from django.db import models


class Photo(models.Model):
    class Meta:
        verbose_name = 'фотография'
        verbose_name_plural = 'фотографии'
    pass


class Album(models.Model):
    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'

    name = models.CharField(max_length=64, help_text='название альбома')
    year = models.PositiveIntegerField(help_text='год')
    photos = models.ManyToManyField(Photo)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
