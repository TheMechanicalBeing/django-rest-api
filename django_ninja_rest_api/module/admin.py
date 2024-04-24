from django.contrib import admin

from .forms import MenuForm
from .models import Menu


class MenuAdmin(admin.ModelAdmin):
    form = MenuForm


admin.site.register(Menu, MenuAdmin)
