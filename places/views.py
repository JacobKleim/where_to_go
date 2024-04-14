from django.shortcuts import render
from django.shortcuts import get_object_or_404
from models import Place, Image

# def get_place(request):
#     places = Place.objects.all()
#     mesta = []
#     for place in places:
#         place_data = {
#             "type": "Feature",
#             "geometry": {
#                 "type": "Point",
#                 "coordinates": [place.lng, place.lat]
#             },
#             "properties": {
#                 "title": place.title,
#                 "placeId": place.id,
#                 "detailsUrl": ""
#             }
#         }
#         mesta.append(place_data)

#     return render(request, 'index.html', context={'places': mesta})

