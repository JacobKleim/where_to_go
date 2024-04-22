from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http.response import JsonResponse

from places.models import Place


def get_place(request, id):
    place = get_object_or_404(Place.objects.prefetch_related('images'), id=id)
    serialized_place = {'title': place.title,
                        'imgs': [image.image.url for image in place.images.all()],
                        'description_short': place.short_description,
                        'description_long': place.long_description,
                        'coordinates': {
                                    'lng': place.lng,
                                    'lat': place.lat,
                                }
                        }
    return JsonResponse(serialized_place,
                        json_dumps_params={'indent': 2, 'ensure_ascii': False},
                        safe=False)


def show_start_page(request):
    places = Place.objects.all()
    places_geojson = {
        'type': 'FeatureCollection',
        'features': [
            {
                'type': 'Feature',
                'geometry': {
                    'type': 'Point',
                    'coordinates': [place.lng, place.lat]
                },
                'properties': {
                    'title': place.title,
                    'placeId': place.id,
                    'detailsUrl': reverse(get_place, kwargs={'id': place.id}),
                }
            }
            for place in places
        ]
    }

    return render(request, 'index.html', {'places_geojson': places_geojson})
