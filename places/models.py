from django.db import models


class Place(models.Model):
    title = models.TextField()
    description_short = models.TextField()
    description_long = models.TextField()
    lng = models.DecimalField(max_digits=18, decimal_places=15)
    lat = models.DecimalField(max_digits=18, decimal_places=15)

    def __str__(self):
        return self.title
