lista = []

def menu():
    print("1- Agregar un número a la lista")
    print("2- Agregar un número a la lista según posición")
    print("3- Ver longitud de la lista")
    print("4- Eliminar el último número")
    print("5- Eliminar un número según posición")
    print("6- Contar repeticiones de un número")
    print("7- Salir")

def seleccionarOpcion(opcion):
    if opcion == 1:
        num = int(input("Por favor, ingresa el número: "))
        lista.append(num)
        print("Lista Actualizada: {0}".format(lista))
    elif opcion == 2:
        num = int(input("Por favor, ingresa el número: "))
        indi = int(input("¿En que indice deseas ingresar el número? "))
        lista.insert(num, indi)
    elif opcion == 3:
        print("La longitud de la lista es de {0}".format(len(lista)))
    elif opcion == 4:
        print("Se ha eliminado el número {0}".format(lista.pop()))
    elif opcion == 5:
        num = int(input("Ingrese el indice del número que desea eliminar: "))
        del lista[num]
    elif opcion == 6:
        num = int(input("Ingrese el número: "))
        print("El número {0} se repite {1} vece(s)".format(num, lista.count(num)))

menu()
while True:
    opcion = int(input("Por favor, ingresa una opción: "))
    seleccionarOpcion(opcion)
    if opcion  == 7:
        print("¡¡Gracias por usar nuestros servicios!!")
        break
