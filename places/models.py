from django.db import models

from tinymce.models import HTMLField


class Place(models.Model):
    title = models.TextField(verbose_name='Название', unique=True)
    short_description = models.TextField(verbose_name='Короткое описание',
                                         blank=True)
    long_description = HTMLField(verbose_name='Длинное описание',
                                 blank=True)
    lng = models.DecimalField(max_digits=18,
                              decimal_places=15,
                              verbose_name='Долгота')
    lat = models.DecimalField(max_digits=18,
                              decimal_places=15,
                              verbose_name='Широта')

    class Meta:
        ordering = ['id']
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return self.title


class Image(models.Model):
    image = models.ImageField(verbose_name='Изображение', unique=True)
    place = models.ForeignKey(
        Place, related_name='images',
        on_delete=models.CASCADE,
        verbose_name='Место')
    number = models.PositiveIntegerField(verbose_name='Номер',
                                         null=True,
                                         blank=True,
                                         db_index=True)

    class Meta:
        ordering = ['place', 'number']
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return f'{self.number} {self.place.title}'
