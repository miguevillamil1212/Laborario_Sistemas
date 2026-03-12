# Sistema Distribuido de Citas Médicas

## Descripción del Proyecto

Este proyecto implementa un **sistema distribuido de gestión de citas médicas** basado en una arquitectura de **microservicios**. Cada microservicio se encarga de una funcionalidad específica del sistema y se comunica con los demás mediante **API REST** utilizando HTTP.

El objetivo del laboratorio es comprender cómo funcionan los sistemas distribuidos, la comunicación entre servicios y la gestión de datos en una arquitectura desacoplada.

El sistema fue desarrollado utilizando el framework **FastAPI** y una base de datos **MariaDB**, ejecutándose en el sistema operativo **Fedora Linux**.

---

# Documentación

**IP:** `172.16.0.134` | **Puerto:** `8003` | **URL base:** `http://172.16.0.134:8003`

---

## 1. Registrar Paciente

**Endpoint:** `POST /pacientes`

**Parámetros (body JSON):**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| nombre | string | Nombre completo del paciente |
| documento | string | Número de documento |

**Ejemplo request:**
```json
{
  "nombre": "Juan Perez",
  "documento": "123456789"
}
```

**Ejemplo response:**
```json
{
  "mensaje": "Paciente registrado"
}
```

---

## 2. Consultar Paciente

**Endpoint:** `GET /pacientes/{id}`

**Parámetros (URL):**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | int | ID del paciente |

**Ejemplo request:**
```
GET http://172.16.0.134:8003/pacientes/1
```

**Ejemplo response:**
```json
{
  "id": 1,
  "nombre": "Juan Perez",
  "documento": "123456789"
}
```

---

## 3. Crear Cita

**Endpoint:** `POST /citas`

**Parámetros (body JSON):**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| paciente_id | int | ID del paciente |
| fecha | string | Fecha y hora de la cita (YYYY-MM-DD HH:MM) |

**Ejemplo request:**
```json
{
  "paciente_id": 1,
  "fecha": "2026-04-01 10:00"
}
```

**Ejemplo response:**
```json
{
  "mensaje": "Cita creada"
}
```

---

## 4. Consultar Citas

**Endpoint:** `GET /citas/{paciente_id}`

**Parámetros (URL):**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| paciente_id | int | ID del paciente |

**Ejemplo request:**
```
GET http://172.16.0.134:8003/citas/1
```

**Ejemplo response:**
```json
[
  {
    "id": 1,
    "paciente_id": 1,
    "fecha": "2026-04-01 10:00:00",
    "estado": "activa"
  }
]
```

---

## 5. Cancelar Cita

**Endpoint:** `DELETE /citas/{id}`

**Parámetros (URL):**
| Campo | Tipo | Descripción |
|-------|------|-------------|
| id | int | ID de la cita |

**Ejemplo request:**
```
DELETE http://172.16.0.134:8003/citas/1
```

**Ejemplo response:**
```json
{
  "mensaje": "Cita cancelada"
}
```

---

## Documentación interactiva

Swagger UI disponible en: `http://172.16.0.134:8003/docs`

# Arquitectura del Sistema

El sistema sigue una arquitectura basada en microservicios donde cada componente realiza una función específica.

```
Cliente
   │
   ▼
API Gateway
   │
   ├── Microservicio Pacientes
   ├── Microservicio Crear Citas
   ├── Microservicio Consultar Citas
   └── Microservicio Cancelar Citas
            │
            ▼
        Base de Datos
```

Cada microservicio se ejecuta en un puerto independiente y se comunica con los demás a través de solicitudes HTTP.

---

# Tecnologías Utilizadas

* Python
* FastAPI
* MariaDB
* REST API
* Uvicorn
* Visual Studio Code
* Fedora Linux

---

# Estructura del Proyecto

```
microservicio_citas
│
├── requirements.txt
├── README.md
│
└── app
    │
    ├── main.py
    ├── database.py
    ├── schemas.py
    └── crud.py
```

Descripción de los archivos:

| Archivo     | Descripción                                     |
| ----------- | ----------------------------------------------- |
| main.py     | Define los endpoints del microservicio          |
| database.py | Maneja la conexión con la base de datos         |
| schemas.py  | Define los modelos de datos                     |
| crud.py     | Contiene la lógica de acceso a la base de datos |

---

# Instalación del Proyecto

## 1. Clonar el repositorio

```
git clone <url-del-repositorio>
cd microservicio_citas
```

## 2. Crear entorno virtual

```
python3 -m venv venv
```

Activar el entorno:

```
source venv/bin/activate
```

## 3. Instalar dependencias

```
pip install -r requirements.txt
```

---

# Configuración de la Base de Datos

Ingresar al servidor de base de datos:

```
sudo mariadb
```

Crear base de datos:

```
CREATE DATABASE citas_medicas;
USE citas_medicas;
```

## Tabla pacientes

```
CREATE TABLE pacientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100),
    documento VARCHAR(20)
);
```

## Tabla citas

```
CREATE TABLE citas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    paciente_id INT,
    fecha DATETIME,
    estado VARCHAR(20)
);
```

---

# Ejecución del Microservicio

Ubicarse en la carpeta del proyecto:

```
cd app
```

Ejecutar el servidor:

```
uvicorn main:app --host 0.0.0.0 --port 8003 --reload
```

El servicio quedará disponible en:

```
http://localhost:8003
```

Documentación automática de la API:

```
http://localhost:8003/docs
```

---

# Endpoints Disponibles

## Registrar Paciente

```
POST /pacientes
```

Ejemplo request:

```
{
 "nombre": "Juan Perez",
 "documento": "123456789"
}
```

Respuesta:

```
{
 "mensaje": "Paciente registrado"
}
```

---

## Consultar Paciente

```
GET /pacientes/{id}
```

Ejemplo:

```
GET /pacientes/1
```

Respuesta:

```
{
 "id": 1,
 "nombre": "Juan Perez",
 "documento": "123456789"
}
```

---

## Crear Cita

```
POST /citas
```

Ejemplo request:

```
{
 "paciente_id": 1,
 "fecha": "2026-04-01 10:00"
}
```

Respuesta:

```
{
 "mensaje": "Cita creada"
}
```

---

## Consultar Citas

```
GET /citas/{paciente_id}
```

Ejemplo:

```
GET /citas/1
```

Respuesta:

```
[
 {
  "id": 1,
  "paciente_id": 1,
  "fecha": "2026-04-01 10:00",
  "estado": "activa"
 }
]
```

---

## Cancelar Cita

```
DELETE /citas/{id}
```

Ejemplo:

```
DELETE /citas/1
```

Respuesta:

```
{
 "mensaje": "Cita cancelada"
}
```

---

# Flujo del Sistema

1. El cliente registra un paciente en el sistema.
2. El microservicio de pacientes guarda la información en la base de datos.
3. El cliente solicita crear una cita médica.
4. El microservicio de citas verifica que el paciente exista.
5. Si el paciente existe, la cita se registra en la base de datos.
6. El usuario puede consultar sus citas registradas.
7. El usuario puede cancelar una cita existente.

---

# Comunicación entre Microservicios

Los microservicios se comunican mediante solicitudes HTTP REST.

Ejemplo de verificación de paciente desde el servicio de citas:

```
GET http://localhost:8002/pacientes/{id}
```

Esto permite validar que el paciente exista antes de registrar una cita.

---

# Problema de Concurrencia

Una situación posible en el sistema es cuando dos clientes intentan registrar una cita en el mismo horario simultáneamente.

Esto puede generar una **condición de carrera (race condition)** donde se registran dos citas en el mismo horario.

Para evitar este problema se podrían implementar mecanismos como:

* Bloqueos en base de datos
* Validaciones de disponibilidad
* Control de transacciones

---

# Autor

Proyecto desarrollado para el laboratorio de **Sistemas Distribuidos**.

Estudiante: Miguel Villamil
Semestre: 9
Asignatura: Sistemas Distribuidos
