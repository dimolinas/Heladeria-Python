import sys
from tabulate import tabulate
#Funcion para mostrar el menú
def mostrarMenu():
    titulo = "Administracion de heladeria"
    print(titulo.center(50, "*"), "\n")
    print(
        "Seleccione una opción (1-5) o q para salir\n1.Comprar\n2.Agregar un producto\n3.Ver inventario\n4.Agregrar al inventario\n5.Total de ventas del dia\nq: Salir")
def mostrarTablas(t):
    print(tabulate(t,headers=("N°.","Nombre", "Precio", "Cantidad")))
#Entrada de datos menu principa
def ingresarDatos():
    while True:
        eleccion = input()
        if eleccion == "1" or eleccion == "2" or eleccion == "3" or eleccion == "4" or eleccion == "5":
            return int(eleccion)
            break
        elif eleccion == "q":
            return eleccion
            break
        else:
            print("Entrada invalida. Por favor intente de nuevo")
#menuPrincipal
def elegirMenuPrincipal(p):
    if p == 1:
        venta()
    if p == 2:
        agregarNuevoProducto()
    if p == 3:
        mostrarInventario()
    if p == 4:
        agregarInventario()
    if p == 5:
        print("totla")
    if p == "q":
        sys.exit()
def venta():
    print("Nueva venta\nEscoja un sabor:")
    mostrarTablas(helados)

def agregarNuevoProducto():
    print("Tipo de producto (1 o 2)\n1. Helado\n2. Cobertura\nq. Salir")
    while True:
        seleccion = input()
        if seleccion == "1" or seleccion== "2":
            break
        if seleccion == "q":
            break
    nuevoProducto = []
    print("Ingrese el nombre del producto(Ejemplos: Galletas, M&Ms, etc.): ")
    nuevoProducto.append(input())
    print("Ingrese el valor de la porción: ")
    nuevoProducto.append(int(input()))
    print("Ingrese el numero de porciones disponibles")
    nuevoProducto.append(int(input()))
    if seleccion == "1":
        helados.append(nuevoProducto)
    if seleccion == "2":
        coberturas.append(nuevoProducto)
def mostrarInventario():
    contador = 0
    print("INVENTARIO\n\nHelados")
    mostrarTablas(helados)
    print("\nCoberturas")
    mostrarTablas(coberturas)
    print()
def agregarInventario():
    print("Tipo de producto (1 o 2)\n1. Helado\n2. Cobertura\nq. Salir")
    while True:
        seleccion = input()
        if seleccion == "1" or seleccion== "2":
            break
        if seleccion == "q":
            break
        print("Entrada invalida. Por favor intente de nuevo")



helados = [["Vainilla", 2000, 12],
           ["Chocolate", 1500, 50]]
coberturas = [["M&Ms", 1500, 30],
              ["Galletas", 2500, 40]]
ventasDia = 0

while True:
    mostrarMenu()
    elegirMenuPrincipal(ingresarDatos())


