from ninja import Schema

from module.models import Block, Menu
from content.models import Category


class BlockSchema(Schema):
    class Meta:
        model = Block
        fields = '__all__'


class MenuSchema(Schema):
    class Meta:
        model = Menu
        fields = '__all__'


class CategorySchema(Schema):
    class Meta:
        model = Category
        fields = '__all__'
