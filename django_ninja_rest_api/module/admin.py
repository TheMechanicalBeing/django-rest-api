from django.contrib import admin

from .forms import MenuForm
from .models import Block, Menu


class MenuAdmin(admin.ModelAdmin):
    form = MenuForm


admin.site.register(Menu, MenuAdmin)
admin.site.register(Block)
