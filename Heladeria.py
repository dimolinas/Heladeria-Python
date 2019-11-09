#Funcion para la entrada de enteros a la derecha de cero
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
#Funcion para eliminar cuando se acaban las porciones de un producto
def verificar(t):
    contador = 0
    while contador < len(t):
        if t[contador][2] == 0:
            del t[contador]
            break
        contador += 1
#Funcion que imprime el menu y sus opciones
def mostrarMenu():
    titulo = "Administracion de heladeria"
    print(titulo.center(50, "*"), "\n")
    print("Seleccione una opción (1-5) o q para salir\n1.Comprar\n2.Agregar un producto\n3.Ver inventario\n4.Agregrar al inventario\n5.Total de ventas del dia\nq: Salir")
#Funcion para imprimir elementos de una lista anidada como parametro
def mostrarTablas(t):
    s = 20
    a = 1
    for i in t:
        print(a, end=")")
        for j in i:
            print(j, end=(s - len(str(j))) * " ")
        a += 1
        print()
#Función para imprimir la eleccion de sabor al usuario
def mostrarSeleccion(t,y):
    s = 20
    l = t[y - 1]
    print(y, end=")")
    for i in l:
        print(i, end=(s - len(str(i))) * " ")
    print()
#Funcion de ingreso para el menu principal
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
#Función en la que se escoge, de acuerdo con la entrada del usuario
def elegirMenuPrincipal(p):
    if p == 1:
        if len(helados) > 0:
            venta()
        else:
            print("No hay helados disponibles")
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
#funcion para la compras de helados
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
    mostrarSeleccion(helados,seleccion)
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
        if len(coberturas)> 0:
            print("Escoja  la cobertura")
            mostrarTablas(coberturas)

            while True:
                eleccionCobertura = ingresarEnteros()
                if eleccionCobertura in range(1,len(coberturas)+1):
                    break
                print("Entrada fuera de rango. Intenta de nuevo")

            print("Usted selecciono:")
            mostrarSeleccion(coberturas,eleccionCobertura)
            coberturas[eleccionCobertura-1][2] -= 1
            totalApagar += coberturas[eleccionCobertura-1][1]
        else:
            print("No hay productos de coverturas")
    print("\nEL total a pagar es:                   ",totalApagar)
    totalVentas += totalApagar

    verificar(helados)
    verificar(coberturas)
#Función si el usuario desea ingresar un nuevo producto
def agregarNuevoProducto():

    print("Tipo de producto (1 o 2)\n1. Helado\n2. Cobertura\nq. Salir")

    while True:
        seleccion = input()
        if seleccion == "1" or seleccion== "2":
            break
        if seleccion == "q":
            return False
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
#Muestra los productos
def mostrarInventario():
    print("INVENTARIO\n\nHelados")
    mostrarTablas(helados)
    print("\nCoberturas")
    mostrarTablas(coberturas)
    print()
#Agrega nuevas contidades a los productos ya registrados
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
#Imprime la variable ventas del dia
def ventasDia(a):
    print("Total ventas del día: {}".format(a),"\n")

#Listas
#Nombre,Precio,Cantidad
helados = [["Vainilla", 2000, 12],
           ["Chocolate", 1500, 50]]
coberturas = [["M&Ms", 1500, 30],
              ["Galletas", 2500, 40]]
#Total Ventas del dia
totalVentas = 0

#Ciclo Principal del programa
while True:
    mostrarMenu()
    if elegirMenuPrincipal(ingresarDatos()) :
        break