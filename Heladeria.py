import sys

def mostrarMenu():
    titulo = "Administracion de heladeria"
    print(titulo.center(50, "*"), "\n")
    print(
        "Seleccione una opción (1-5) o q para salir\n1.Comprar\n2.Agregar un producto\n3.Ver inventario\n4.Agregrar al inventario\n5.Total de ventas del dia\nq: Salir")

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

def elegirMenuPrincipal(p):
    if p == 1:
        venta(helados, coberturas)
    if p == 2:
        print("Agregar")
    if p == 3:
        mostrarInventario(helados, coberturas)
    if p == 4:
        print("agregar")
    if p == 5:
        print("totla")
    if p == "q":
        sys.exit()


def venta(h, c):
    print("Nueva venta\nEscoja un sabor:")
    contador = 0
    print("N°) \t Sabor              \t Precio         \t Cantidad")
    while contador < len(helados):
        print(contador + 1, ")", '\t', helados[contador][0], "           ", '\t', helados[contador][1], "         ",
              '\t', helados[contador][2])
        contador += 1
    eleccion = input()


def mostrarInventario(h, c):
    print("INVENTARIO")


# listaHelados
# Nombre, precio, cantidad
helados = [["Vainilla", 2000, 12], ["Chocolate", 1500, 50]]
# listaCoverturas
# Nombre, precio, cantidad
coberturas = [["M&Ms", 1500, 30], ["Galletas", 2500, 40]]

mostrarMenu()
elegirMenuPrincipal(ingresarDatos())