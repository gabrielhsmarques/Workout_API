from typing import Annotated, Optional
from pydantic import Field, PositiveFloat

from workout_api.categorias.schemas import CategoriaIn
from workout_api.centro_treinamento.schemas import CentroTreinamentoIn
from workout_api.contrib.schemas import BaseSchema, OutMixin

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Gabriel', max_length=40)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='11122233344', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example='75')]
    peso: Annotated[PositiveFloat, Field(description='Idade do atleta', example='75.2')]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example='1.91')]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
    categoria: Annotated[CategoriaIn, Field(description='Categoria do atleta')]
    centro_treinamento: Annotated[CentroTreinamentoIn, Field(description='Centro de treinamento do atleta')]

class AtletaIn(Atleta):
    pass

class AtletaOut(AtletaIn, OutMixin):
    pass

class AtletaUpdate(BaseSchema):
    nome: Annotated[Optional[str], Field(None, description='Nome do atleta', example='Gabriel', max_length=40)]
    idade: Annotated[Optional[int], Field(None, description='Idade do atleta', example='75')]
    peso: Annotated[Optional[PositiveFloat], Field(None, description='Idade do atleta', example='75.2')]

class AtletaOutCustom(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Gabriel', max_length=40)]
    centro_treinamento: Annotated[str, Field(description='Nome do centro de treinamento', example='CT Força')]
    categoria: Annotated[str, Field(description='Nome da categoria', example='Pro')]
