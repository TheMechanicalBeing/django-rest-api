from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='uploads/logos')
    parent = models.ForeignKey('self', on_delete=models.RESTRICT, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
