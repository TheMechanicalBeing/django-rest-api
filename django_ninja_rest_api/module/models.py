from django.db import models


def visual_options():
    return {
        'standard': 'Standard',
        'horizontal': 'Horizontal',
        'vertical': 'Vertical',
    }


class Menu(models.Model):
    name = models.CharField(max_length=250, blank=True)
    link = models.URLField(max_length=250, blank=True)
    is_external = models.BooleanField(default=False)
    category = models.ForeignKey('content.Category', on_delete=models.CASCADE, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Menus'
        ordering = ['name']

    def __str__(self):
        if self.name:
            return self.name
        else:
            return f'{self.category.name} (Category reference)'


class Block(models.Model):
    article = models.ManyToManyField('content.Article', blank=True)
    block_visual = models.CharField(max_length=50, choices=visual_options)
    block_position = models.CharField(max_length=50)
    block_row = models.PositiveIntegerField()
    title = models.CharField(max_length=250)
    show_title = models.BooleanField(default=False)

    def __str__(self):
        return self.title
