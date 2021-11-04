import mysql.connector as connector

from Departamento import Departamento
from Empleado import Empleado

def conectar_base_datos(host, user, password, database):
    connection = connector.connect(host=host, user=user, password=password, database=database)
    return connection


def cerrar_conexion(conn):
    if conn is not None:
        conn.close()


def mostrar(lista):
    for elemento in lista:
        print(elemento)


querys = {
    "Employees": "select * from Employees",
    "Departments": "select * from Departments",
    "Employees_by_Department": "select * from Employees where Department = {dato}",
    "Departments_by_budget": "select * from Departments where budget > {dato}"
}


def get(conn, opcion, dato=""):
    mycursor = conn.cursor()
    if (opcion == 1):
        query = querys["Employees"]
    if (opcion == 2):
        query = querys["Departments"]
    if (opcion == 3):
        query = querys["Employees_by_Department"].format(dato=dato)
    if (opcion == 4):
        query = querys["Departments_by_budget"].format(dato=dato)
    mycursor.execute(query)

    return mycursor.fetchall()


def vista():
    print("\nGestion de la empresa\n")
    print("1.- Seleccionar empleados")
    print("2.- Seleccionar departamentos")
    print("3.- Buscar empleados por departamento")
    print("4.- Buscar departamentos por presupuesto mayor que el introducido")
    print("0.- Salir")
    return input()


def menu():
    login = {"host": "localhost", "user": "operator", "password": "pue", "database": "factory"}
    empleados = list()
    departamentos = list()
    continuar = True
    while (continuar):
        try:
            opcion = int(vista())
        except ValueError as ve:
            opcion = -1
            print("No valido")

        conn = conectar_base_datos(**login)
        if (opcion == 1):
            lista = get(conn, 1)
            #for elemento in lista:
            #    empleados.append(Empleado(*elemento))

            mostrar([Empleado(*elemento) for elemento in lista])
        if (opcion == 2):
            lista = get(conn, 2)
            #for elemento in lista:
            #    departamentos.append(Departamento(*elemento))
            mostrar([Departamento(*elemento) for elemento in lista])
        if (opcion == 3):
            lista = get(conn, 3, int(input("introduce el departamento\n")))
            mostrar([Empleado(*elemento) for elemento in lista])
        if (opcion == 4):
                lista = get(conn, 4, int(input("introduce el Presupuesto\n")))
                mostrar([Departamento(*elemento) for elemento in lista])
        if (opcion == 0):
            continuar = False
            conn.close()


if __name__ == "__main__":
    menu()
    pass
