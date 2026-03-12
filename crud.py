from database import get_connection

def crear_paciente(nombre, documento):

    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO pacientes (nombre, documento) VALUES (%s,%s)"
    cursor.execute(sql, (nombre, documento))

    conn.commit()

    return {"mensaje": "Paciente registrado"}


def obtener_paciente(id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM pacientes WHERE id=%s"
    cursor.execute(sql, (id,))

    paciente = cursor.fetchone()

    return paciente


def crear_cita(paciente_id, fecha):

    conn = get_connection()
    cursor = conn.cursor()

    sql = "INSERT INTO citas (paciente_id, fecha, estado) VALUES (%s,%s,'activa')"
    cursor.execute(sql, (paciente_id, fecha))

    conn.commit()

    return {"mensaje": "Cita creada"}


def obtener_citas(paciente_id):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = "SELECT * FROM citas WHERE paciente_id=%s"
    cursor.execute(sql, (paciente_id,))

    citas = cursor.fetchall()

    return citas


def cancelar_cita(id):

    conn = get_connection()
    cursor = conn.cursor()

    sql = "DELETE FROM citas WHERE id=%s"
    cursor.execute(sql, (id,))

    conn.commit()

    return {"mensaje": "Cita cancelada"}

def validar_paciente(id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = "SELECT 1 FROM pacientes WHERE id = %s"
    cursor.execute(sql, (id,))

    existe = cursor.fetchone()

    cursor.close()
    conn.close()

    return existe is not None
