from django.shortcuts import render, get_object_or_404
from django.http.response import JsonResponse

import json

from places.models import Place


def show_start_page(request):
    places = Place.objects.all()
    places_geojson = {
        "type": "FeatureCollection",
        "features": []
    }
    for place in places:
        images_urls = [image.image.url for image in place.images.all()]
        print(images_urls)
        images_urls_json = json.dumps(images_urls)
        print(images_urls)
        place_data = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lng, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": 
                "static/places/moscow_legends.json",
                    # {
                    #     "title": place.title,
                    #     "imgs": images_urls_json,
                    #     "description_short": place.description_short,
                    #     "description_long": place.description_long,
                    #     "coordinates": {
                    #         "lng": place.lng,
                    #         "lat": place.lat,
                    #     }
                    # },
            }
        }
        places_geojson["features"].append(place_data)

    return render(request, 'index.html', {'places_geojson': places_geojson})


def get_place(request, id):
    place = get_object_or_404(Place, id=id)
    serialized_place = {'title': place.title,
                        'imgs': [image.image.url for image in place.images.all()],
                        "description_short": place.description_short,
                        "description_long": place.description_long,
                        "coordinates": {
                                    "lng": place.lng,
                                    "lat": place.lat,
                                }
                        }
    return JsonResponse(serialized_place,
                        json_dumps_params={'indent': 2, 'ensure_ascii': False},
                        safe=False)