def ingresarEnteros():
    while True:
        entrada = input()
        try:
            entrada = int(entrada)
            if entrada > 0:
                return entrada
            else:
                print("Entrada Invalida.Por favor intente de nuevo")
        except ValueError:
            print("Entrada Invalida. Por favor intente de nuevo")
def mostrarMenu():
    titulo = "Administracion de heladeria"
    print(titulo.center(50, "*"), "\n")
    print("Seleccione una opción (1-5) o q para salir\n1.Comprar\n2.Agregar un producto\n3.Ver inventario\n4.Agregrar al inventario\n5.Total de ventas del dia\nq: Salir")
def mostrarTablas(t):
    s = 20
    a = 1
    for i in t:
        print(a, end=")")
        for j in i:
            print(j, end=(s - len(str(j))) * " ")
        a += 1
        print()
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
        venta()
    if p == 2:
        agregarNuevoProducto()
    if p == 3:
        mostrarInventario()
    if p == 4:
        agregarInventario()
    if p == 5:
        ventasDia(totalVentas)
    if p == "q":
        return True
def venta():

    global totalVentas
    print("Nueva venta\nEscoja un sabor:")
    mostrarTablas(helados)

    while True:
        seleccion = ingresarEnteros()
        if seleccion in range(1,len(helados)+1):
            break
        print("Entrada fuera de rango. Intenta de nuevo")

    print("Usted seleccionó:")
    print(seleccion, "       ", helados[seleccion - 1][0], "         ", helados[seleccion - 1][1], "       ", helados[seleccion - 1][2])
    print("\n ¿Cuantas porciones?:")

    while True:
        porciones = ingresarEnteros()
        if porciones > helados[seleccion-1][2]:
            print("No hay esa cantidad de porciones, ingresa menos por favor ")
        else:
            break
    helados[seleccion-1][2] -= porciones
    totalApagar = porciones * helados[seleccion-1][1]
    print("\n¿Desea cobertura?(s/n):")

    while True:
        seleccionCobertura = input()
        if seleccionCobertura == "s" or seleccionCobertura == "n":
            break
        print("Entrada Invalidad. Intenta de nuevo")

    if seleccionCobertura == "s":
        print("Escoja  la cobertura")
        mostrarTablas(coberturas)

        while True:
            eleccionCobertura = ingresarEnteros()
            if eleccionCobertura in range(1,len(coberturas)+1):
                break
            print("Entrada fuera de rango. Intenta de nuevo")

        print("Usted selecciono:")
        print(eleccionCobertura, "       ", coberturas[eleccionCobertura - 1][0], "         ", coberturas[eleccionCobertura - 1][1], "       ", coberturas[eleccionCobertura - 1][2])
        coberturas[seleccion-1][2] -= 1
        totalApagar += coberturas[eleccionCobertura-1][1]

    print("\nEL total a pagar es:                   ",totalApagar)
    totalVentas += totalApagar
def agregarNuevoProducto():

    print("Tipo de producto (1 o 2)\n1. Helado\n2. Cobertura\nq. Salir")

    while True:
        seleccion = input()
        if seleccion == "1" or seleccion== "2":
            break
        if seleccion == "q":
            break
        print("Entrada invalida. Por favor intente de nuevo")

    nuevoProducto = []
    ingreso = True
    nombre = input("Ingrese el nombre del producto(Ejemplos: Galletas, M&Ms, etc.): \n")

    if seleccion == "1":

        for i in range(0, len(helados)):
            if nombre == helados[i][0]:
                print("Este sabor de helado  ya esta registrado\n")
                ingreso = False

    if seleccion == "2":

        for i in range(0,len(coberturas)):
            if nombre == coberturas[i][0]:
                print("Este sabor de cobertura ya esta registrado\n")
                ingreso = False

    if ingreso == True:
        nuevoProducto.append(nombre)
        print("Ingrese el valor de la porción: ")
        nuevoProducto.append(ingresarEnteros())

        print("Ingrese el numero de porciones disponibles")
        nuevoProducto.append(ingresarEnteros())

        if seleccion == "1":
            helados.append(nuevoProducto)

        if seleccion == "2":
            coberturas.append(nuevoProducto)
def mostrarInventario():
    print("INVENTARIO\n\nHelados")
    mostrarTablas(helados)
    print("\nCoberturas")
    mostrarTablas(coberturas)
    print()
def agregarInventario():
    print("Tipo de producto (1 o 2)\n1. Helado\n2. Cobertura\nq. Salir")
    while True:
        seleccion = input()
        if seleccion == "1" or   seleccion== "2":
            break
        if seleccion == "q":
            break
        print("Entrada invalida. Por favor intente de nuevo")
    if seleccion == "1":
        mostrarTablas(helados)
        print("\nSeleccione un producto: ")

        while True:
            entrada = int(input())
            if entrada in range(1,len(helados)+1):
                break
            print("Entrada invalida. Por favor intente de nuevo")

        print("Usted selecciono: ")
        print(entrada,"       ",helados[entrada-1][0],"       ",helados[entrada-1][1], "         ",helados[entrada-1][2])
        print("\nIngrese la cantidad de personas a registrar:")
        nuevasPorciones = ingresarEnteros()
        helados[entrada-1][2] += nuevasPorciones

    if seleccion == "2":
        mostrarTablas(coberturas)
        print("\nSeleccione un producto: ")

        while True:
            entrada = int(input())
            if entrada in range(1,len(helados)+1):
                break
            print("Entrada invalida. Por favor intente de nuevo")

        print("Usted selecciono: ")
        print(entrada,"       ",coberturas[entrada-1][0], "         ",coberturas[entrada-1][1], "       ", coberturas[entrada-1][2])
        print("\nIngrese la cantidad de porciones a registrar:")
        nuevasPorciones = ingresarEnteros()
        coberturas[entrada-1][2] += nuevasPorciones
def ventasDia(a):
    print("Total ventas del día: {}".format(a),"\n")

helados = [["Vainilla", 2000, 12],
           ["Chocolate", 1500, 50]]
coberturas = [["M&Ms", 1500, 30],
              ["Galletas", 2500, 40]]
totalVentas = 0

while True:
    mostrarMenu()
    if elegirMenuPrincipal(ingresarDatos()) :
        break


