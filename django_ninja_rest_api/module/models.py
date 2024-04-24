from django.db import models
from django.core.exceptions import ValidationError


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
