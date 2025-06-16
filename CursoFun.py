import sqlite3
import Validar

DB_FILE = "escueladb.db"

def cargar_curso(): #pide el nombre como input
    nombre = Validar.input_nombre_vacio()
    return nombre

#print(cargar_curso())

def agregar_curso(nombre): #dandole el nombre como str lo inserta en la tabla curso
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO curso (nombre) VALUES (?)",
        (nombre,)
    )
    conn.commit()
    conn.close()

def listar_cursos(): #devuelve todos los cursos en tabla curso como una lista de tuplas
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM curso")
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_curso_id(id_curso): #devuelve el curso del ID(Parametro) como una tupla
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM curso WHERE id_curso = (?)",(id_curso,))
    vuelta = traer.fetchone()
    conn.commit()
    conn.close()
    return vuelta

def listar_curso_idall(id_curso): #devuelve el curso del ID(Parametro) como una lista de tupla
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM curso WHERE id_curso = (?)",(id_curso,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def listar_curso_nombre(nombre): #devuelve el curso del nombre(Parametro) como una lista de tuplas con todos los cursos con ese nombre
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM curso WHERE nombre = (?)",(nombre,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

def modificar_curso_nombre(id_curso, nombre): #modificar el nombre de un curso con ID_curso como parametros
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    try:
        cur.execute("UPDATE curso SET nombre = (?) WHERE id_curso = (?)",(nombre, id_curso))
        conn.commit()
        print("Cambio realizado correctamente")
    except:
        print("Hubo un error")
    conn.close()
    
# print(listar_cursos())
# modificar_curso_nombre(12,"Séptimo")
# print(listar_cursos())

def existe_curso_id(id_curso): #valida si existe curso con ese id
    intentos = 4
    while True:
        if Validar.existe_en_tabla("curso","id_curso",id_curso) != False:
            #print(listar_curso_id(id_curso))
            return listar_curso_id(id_curso)
        else:
            print(f"-"*100)
            print("No existe curso con ese ID")
            intentos -=1
            print(f"quedan {intentos} intento/s")
            if intentos == 0:
                return False
            id_curso = Validar.input_ent("Ingrese el ID de un Curso válido: ")
            continue

#print(existe_curso_id(123))