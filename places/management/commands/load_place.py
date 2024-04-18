import os
import requests
from django.conf import settings
from django.core.management.base import BaseCommand
from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load places data from JSON files in a GitHub folder'

    def add_arguments(self, parser):
        parser.add_argument(
            'github_repo',
            type=str,
            help='GitHub repository name (username/repository)')
        parser.add_argument(
            'folder_path',
            type=str,
            help='Path to the folder containing JSON files on GitHub')

    def handle(self, *args, **options):
        github_repo = options['github_repo']
        folder_path = options['folder_path']

        url = f'https://api.github.com/repos/{github_repo}/contents/{folder_path}'
        response = requests.get(url)
        if response.status_code != 200:
            self.stdout.write(
                self.style.ERROR(f'Failed to fetch files '
                                 f'from GitHub API: {url}'))
            return

        files = response.json()
        media_folder = os.path.join(settings.MEDIA_ROOT)
        os.makedirs(media_folder, exist_ok=True)

        for file in files:
            if file.get('type') != 'file' or not file.get(
                    'name').endswith('.json'):
                continue

            json_url = file['download_url']
            response = requests.get(json_url)

            if response.status_code != 200:
                self.stdout.write(
                    self.style.ERROR(f'Failed to load data '
                                     f'from URL: {json_url}'))
                continue

            try:
                place_data = response.json()
                place, created = Place.objects.get_or_create(
                    title=place_data['title'],
                    description_short=place_data['description_short'],
                    description_long=place_data['description_long'],
                    lng=place_data['coordinates']['lng'],
                    lat=place_data['coordinates']['lat']
                )

                image_urls = place_data.get('imgs', [])
                for number, image_url in enumerate(image_urls, start=1):
                    response = requests.get(image_url)
                    if response.status_code != 200:
                        self.stdout.write(
                            self.style.WARNING(
                                f'Image file not found '
                                f'for place {place.title}'))
                        continue

                    image_filename = os.path.basename(image_url)
                    image_path = os.path.join(media_folder, image_filename)

                    with open(image_path, 'wb') as image_file:
                        image_file.write(response.content)

                    image = Image.objects.create(
                        place=place,
                        number=number
                    )
                    image.image.name = os.path.join(image_filename)
                    image.save()

                    self.stdout.write(
                        self.style.SUCCESS(
                            f'Added image {image_filename} '
                            f'to place {place.title}'
                        )
                    )
            except Exception as e:
                self.stdout.write(
                    self.style.ERROR(e))
