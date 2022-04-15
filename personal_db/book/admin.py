from django.contrib import admin
from .models import Notebook


class NotebookAdmin(admin.ModelAdmin):
    """
    Класс для настройки отображения моделей в
    админ-панели.
    """
    list_display = ()
    list_display_links = ()
    search_fields = ()


admin.site.register(Notebook, NotebookAdmin)
