from typing import Annotated
from pydantic import Field, PositiveFloat

from workout_api.contrib.schemas import BaseSchema

class AtletaSchema(BaseSchema):
    nome: Annotated[str, Field(description='Nome do atleta', example='Gabriel', max_length=40)]
    cpf: Annotated[str, Field(description='CPF do atleta', example='11122233344', max_length=11)]
    idade: Annotated[int, Field(description='Idade do atleta', example='75')]
    peso: Annotated[PositiveFloat, Field(description='Idade do atleta', example='75.2')]
    altura: Annotated[PositiveFloat, Field(description='Altura do atleta', example='1.91')]
    sexo: Annotated[str, Field(description='Sexo do atleta', example='M', max_length=1)]
