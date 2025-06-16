import sqlite3
import Validar as v

DB_FILE = "escueladb.db"

while True:
    print("Cómo desea acceder")
    print("1) Administrativo")
    print("2) Profesor")
    print("3) Alumno")
    print("4) salir")
    opcion = v.input_opcion("Elegir una opción con el número respectivo",4)
    if opcion == 1:
        print("bienvenido Administrativo")
        continue
    elif opcion == 2:
        print("bienvenido Profesor")
        continue
    elif opcion == 3:
        print("bienvenido Alumno")
        continue
    elif opcion == 4:
        print("Gracias por usar este sistema.")
        break