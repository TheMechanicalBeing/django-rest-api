from ninja import NinjaAPI

api = NinjaAPI()


@api.get('/helloworld')
def first(request):
    return {'Hello': 'World!'}
