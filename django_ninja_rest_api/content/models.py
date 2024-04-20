from django.db import models
from treebeard.mp_tree import MP_Node


class Category(MP_Node):
    name = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='uploads/logos')

    node_order_by = ['name']

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
