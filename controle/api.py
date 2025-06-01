from ninja import NinjaAPI
from .schema import UberSchemain, UberSchemaout
from .models import Uber


api = NinjaAPI()
'''API PARA ADICIONAR O DADOS DO DIA'''
@api.post("/add",response={201: UberSchemain})
def adicionar(request,dados:UberSchemain) -> Uber:
    dados = Uber.objects.create(**dados.dict())
    return dados

'''API PARA MOSTRAR O GANHO FINAL'''
@api.get("/listar", response=list[UberSchemaout])
def listar(request):
    dados = Uber.objects.all()
    for c in dados:
        c.resultado()
    return dados

