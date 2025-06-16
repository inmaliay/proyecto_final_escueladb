import sqlite3
import ProfesorFun as p
import Validar as v

DB_FILE = "escueladb.db"

def cargar_materia(): #pide el nombre como input el nombre de materia y ID profesor,  #devuelve ambos como una lista
    vuelta = []
    nombre = v.input_nombre_vacio("Nombre de la Materia: ")
    profes_lista = p.listar_profesores()
    print(profes_lista)
    while True:
        id_profesor = v.input_ent("ID del profesor a cargo: ")
        existe = p.existe_profesor_id(id_profesor)
        if existe != False:
            vuelta.append(nombre)
            vuelta.append(existe[0])
            #print(vuelta)
            return vuelta #vuelta[0] = nombre(materia) y vuelta[1] = id_profesor
        else:
            print(f"-"*100)
            print("Error, no existe profesor con ese ID")
            print(f"-"*100)
            return False

#print(cargar_materia())

def agregar_materia(nombre, id_profesor): #agrega materias con nombre(materia) y ID del profesor a cargo (id_profesor)
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO materia (nombre, id_profesor) VALUES (?, ?)",
        (nombre, id_profesor)
    )
    conn.commit()
    conn.close()

# materia_profe = cargar_materia()
# agregar_materia(materia_profe[0], materia_profe[1])

def listar_materias(): #lista todas las materias
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM materia")
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

#print(listar_materias())

def listar_materia_id(id_materia): #lista toda las materia con ID
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM materia WHERE id_materia = (?)",(id_materia,))
    vuelta = traer.fetchone()
    conn.commit()
    conn.close()
    return vuelta

#print(listar_materia_id(1))

def listar_materia_idall(id_materia): #lista toda las materia con ID
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    traer = cur.execute("SELECT * FROM materia WHERE id_materia = (?)",(id_materia,))
    vuelta = traer.fetchall()
    conn.commit()
    conn.close()
    return vuelta

#print(listar_materia_idall(1))