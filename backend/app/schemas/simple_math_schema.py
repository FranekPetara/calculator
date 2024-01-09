from pydantic import BaseModel, validator
from fastapi import Query

class AdditionInputSchema(BaseModel):
    x: float
    y: float


class SubtractInputSchema(BaseModel):
    x: float
    y: float


class MultiplyInputSchema(BaseModel):
    x: float
    y: float


class DivideInputSchema(BaseModel):
    x: float
    y: float