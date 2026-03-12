from pydantic import BaseModel

class Paciente(BaseModel):
    nombre: str
    documento: str


class Cita(BaseModel):
    paciente_id: int
    fecha: str