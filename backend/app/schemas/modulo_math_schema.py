from pydantic import BaseModel, validator

class ModuloInputSchema(BaseModel):
    x: float
    y: float