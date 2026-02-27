from typing import Annotated
from pydantic import UUID4, Field

from workout_api.contrib.schemas import BaseSchema


class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='Alpha', max_length=20)]
    endereco: Annotated[str, Field(description='Endereco do centro de treinamento', example='Rua b, 125', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do centro de treinamento', example='Jose Augusto', max_length=30)]\
    
class CentroTreinamentoAtleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do Centro de treinamento', examples='CT', max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador do Centro de treinamento')]