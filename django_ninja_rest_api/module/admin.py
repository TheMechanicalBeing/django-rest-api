from django.contrib import admin

from .forms import MenuForm, BlockForm
from .models import Block, Menu


class ArticleInline(admin.TabularInline):
    model = Block.articles.through
    extra = 2


class MenuAdmin(admin.ModelAdmin):
    form = MenuForm


class BlockAdmin(admin.ModelAdmin):
    fields = ('block_visual', 'block_position', 'block_row', 'title', 'show_title')
    form = BlockForm
    inlines = [
        ArticleInline,
    ]


admin.site.register(Menu, MenuAdmin)
admin.site.register(Block, BlockAdmin)
