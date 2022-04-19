from django.db import models


class Album(models.Model):
    class Meta:
        verbose_name = 'альбом'
        verbose_name_plural = 'альбомы'

    pass
