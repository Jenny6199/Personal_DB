from django.db import models


class Notebook(models.Model):
    """
    Модель хранения данных.
    """
    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'
