from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from treebeard.mp_tree import MP_Node



class Category(MP_Node):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='uploads/logos', blank=True, null=True)

    node_order_by = ['name']

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=320)

    class Meta:
        verbose_name_plural = 'Tags'

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=500)
    description = HTMLField()
    post_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('users.CustomUser', on_delete=models.RESTRICT, blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to='uploads/articles', blank=True, null=True)
    publish = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Articles'

    def __str__(self):
        return self.title
