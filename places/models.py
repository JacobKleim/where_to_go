from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.TextField()
    description_short = models.TextField()
    description_long = HTMLField()
    lng = models.DecimalField(max_digits=18, decimal_places=15)
    lat = models.DecimalField(max_digits=18, decimal_places=15)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField()
    place = models.ForeignKey(
        Place, related_name='images',
        on_delete=models.CASCADE)
    number = models.PositiveIntegerField()

    class Meta:
        ordering = ['place', 'number']

    def __str__(self):
        return f'{self.number} {self.place.title}'
