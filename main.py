from fastapi import FastAPI, HTTPException
import requests

from schemas import Paciente, Cita
import crud

app = FastAPI()


@app.get("/")
def home():
    return {"mensaje": "Microservicio funcionando"}

@app.post("/pacientes")
def registrar_paciente(paciente: Paciente):

    return crud.crear_paciente(
        paciente.nombre,
        paciente.documento
    )

@app.get("/pacientes/{id}")
def consultar_paciente(id: int):

    paciente = crud.obtener_paciente(id)

    if not paciente:
        raise HTTPException(status_code=404, detail="Paciente no encontrado")

    return paciente

@app.post("/citas")
def crear_cita(cita: Cita):

    if not crud.validar_paciente(cita.paciente_id):
        raise HTTPException(status_code=404, detail="Paciente no encontrado")

    return crud.crear_cita(
        cita.paciente_id,
        cita.fecha
    )

@app.get("/citas/{paciente_id}")
def consultar_citas(paciente_id: int):

    return crud.obtener_citas(paciente_id)


@app.delete("/citas/{id}")
def cancelar_cita(id: int):

    return crud.cancelar_cita(id)