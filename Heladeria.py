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
    for i in range(0,len(t)):
        print(i+1,end="")
        for j in range(0,len(t[i])):
            print("     ",t[i][j],end="")
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
        seleccion = int(input())
        if seleccion in range(1,len(helados)+1):
            break
        print("Entrada invalida. Por favor intente de nuevo")
    print("Usted seleccionó:")
    print(helados[seleccion - 1][0], "       ", helados[seleccion - 1][1], "         ", helados[seleccion - 1][2], "       ", helados[seleccion - 1][3])
    print("\n ¿Cuantas porciones?:")
    while True:
        porciones = ingresarEnteros()
        if porciones > helados[seleccion-1][3]:
            print("No hay esa cantidad de porciones, ingresa menos por favor ")
        else:
            break
    print("\n¿Desea cobertura?(s/n):")
    while True:
        seleccionCobertura = input()
        if seleccionCobertura == "s" or seleccionCobertura == "n":
            break
        print("Entrada Invalidad. Intenta de nuevo")
    if seleccionCobertura == "n":
        totalApagar = porciones * helados[seleccion-1][2]
        totalVentas += totalApagar
    if seleccionCobertura == "s":
        print("Escoja  la cobertura")
        mostrarTablas(coberturas)
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
    print("Ingrese el nombre del producto(Ejemplos: Galletas, M&Ms, etc.): ")
    nuevoProducto.append(input())
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
        print(helados[entrada-1][0],"       ",helados[entrada-1][1], "         ",helados[entrada-1][2], "       ", helados[entrada-1][3])
        print("Ingrese la cantidad de personas a registrar: \n")
        nuevasPorciones = ingresarEnteros()
        helados[entrada-1][3] += nuevasPorciones
    if seleccion == "2":
        mostrarTablas(coberturas)
        while True:
            entrada = int(input())
            if entrada in range(1,len(helados)+1):
                break
            print("Entrada invalida. Por favor intente de nuevo")
        print("Usted selecciono: ")
        print(coberturas[entrada-1][0],"       ",coberturas[entrada-1][1], "         ",coberturas[entrada-1][2], "       ", coberturas[entrada-1][2])
        print("Ingrese la cantidad de porciones a registrar:\n")
        nuevasPorciones = ingresarEnteros()
        coberturas[entrada-1][3] += nuevasPorciones
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


