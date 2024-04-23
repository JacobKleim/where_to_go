import os
import requests

from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand

from places.models import Place, Image


class Command(BaseCommand):
    help = 'Load places data from JSON files in a GitHub folder'

    def add_arguments(self, parser):
        parser.add_argument(
            'url',
            type=str,
            help='Url with json-data')

    def handle(self, *args, **options):
        url = options['url']
        response = requests.get(url)
        if response.status_code != 200:
            self.stdout.write(
                self.style.ERROR(f'Failed to fetch files '
                                 f'from GitHub API: {url}'))
            return

        if response.status_code != 200:
            self.stdout.write(
                self.style.ERROR(f'Failed to load data '
                                 f'from URL: {url}'))

        try:
            raw_place = response.json()
            place, created = Place.objects.get_or_create(
                lng=raw_place['coordinates']['lng'],
                lat=raw_place['coordinates']['lat'],
                defaults={
                    'title': raw_place['title'],
                    'short_description': raw_place['description_short'],
                    'long_description': raw_place['description_long']
                }
            )

            image_urls = raw_place.get('imgs', [])
            for number, image_url in enumerate(image_urls, start=1):
                response = requests.get(image_url)
                image_filename = os.path.basename(image_url)

                existing_image = Image.objects.filter(
                    place=place,
                    image=image_filename).first()

                if existing_image:
                    self.stdout.write(
                        self.style.WARNING(
                            f'Image {image_filename} already '
                            f'exists for place {place.title}. Skipping...'
                        )
                    )
                    continue

                image = Image.objects.create(
                    place=place,
                    number=number
                )

                image.image.save(image_filename, ContentFile(response.content))

                self.stdout.write(
                    self.style.SUCCESS(
                        f'Added image {image_filename} '
                        f'to place {place.title}'
                    )
                )
        except Exception as e:
            self.stdout.write(
                self.style.ERROR(e))
