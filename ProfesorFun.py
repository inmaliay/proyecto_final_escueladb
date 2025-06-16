import sqlite3
import Validar

DB_FILE = "escueladb.db"

def cargar_profesor(): #acepta datos como input
    vuelta = []
    nombre = Validar.input_nombre("Ingrese el nombre del profesor (sin espacios): ")
    apellido = Validar.input_apellido("Ingrese el apellido del profesor: ")
    dni = Validar.input_dni("Ingrese el DNI del profesor (sin puntos ni espacios): ")
    clave = Validar.input_clave("Ingrese la Clave (sin puntos ni espacios, solo 4 números): ")
    vuelta.append(nombre)
    vuelta.append(apellido)
    vuelta.append(dni)
    vuelta.append(clave)
    #print(vuelta)
    return vuelta #vuelta[0] = nombre(prof.) / vuelta[1] = apellido(prof.) / vuelta[2] = dni(prof.) int / vuelta[3] = clave(prof.)

print(cargar_profesor())

def agregar_profesor(nombre, apellido, dni, clave): #carga los datos en la base de datos
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO profesor (nombre, apellido, dni, clave) VALUES (?, ?, ?, ?)",
        (nombre, apellido, dni, clave)
    )
    conn.commit()
    conn.close()

def listar_profesores():  #devuelve todos los profesores en tabla Profesor como una lista de tuplas
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM profesor")
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_sus_materias(id_profesor): #ingresando ID profe vuelve todas las materias que da
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM materia WHERE id_profesor = (?)",(id_profesor,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_profesor_id(id_profesor):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM profesor WHERE id_profesor = (?)",(id_profesor,))
    vuelta = traer.fetchone()
    conn.commit()
    conn.close()
    return vuelta

def listar_profesor_idall(id_profesor):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM profesor WHERE id_profesor = (?)",(id_profesor,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_profesores_apellido(apellido):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM profesor WHERE apellido = (?)",(apellido,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_profesores_nombre(nombre):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM profesor WHERE nombre = (?)",(nombre,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_profesores_dni(dni):
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM profesor WHERE dni = (?)",(dni,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def existe_profesor_id(id_profesor): #valida si existe un profesor con ese id (parametro) y Da 3 intentos antes de devolver falso
    intentos = 4
    while True:
        if Validar.existe_en_tabla("profesor","id_profesor",id_profesor) != False:
            #print(listar_curso_id(id_curso))
            return listar_profesor_id(id_profesor)
        else:
            print(f"-"*100)
            print("No existe Profesor con ese ID")
            intentos -=1
            print(f"quedan {intentos} intento/s")
            if intentos == 0:
                return False
            id_profesor = Validar.input_ent("Ingrese el ID de un Profesor válido: ")
            continue

#print(existe_profesor_id(123))