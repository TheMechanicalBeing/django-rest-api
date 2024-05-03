from ninja import NinjaAPI

api = NinjaAPI()


@api.get('/blocks')
def blocks_get(request, category: str = None, tag: str = None, block_id: int = None):
    return {'API Service': 'BLOCKS'}


@api.get('/menus')
def menus_get(request, category: str = None, menu_id: int = None):
    return {'API Service': 'MENUS'}


@api.get('/categories')
def categories_get(request, category_id: int = None):
    return {'API Service': 'CATEGORIES'}
