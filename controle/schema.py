from ninja import ModelSchema
from .models import Uber

class UberSchemain(ModelSchema):
    class Config:
        model = Uber
        model_fields = ['data_criacao','gasolina','ganho', 'km']


class UberSchemaout(ModelSchema):
    class Config:
        model = Uber
        model_fields = ['ganho','data_criacao']

