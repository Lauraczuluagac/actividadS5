def ejercicio1():
  
    
    edad = int(input("Ingrese su edad: "))
    if edad >= 18:
        print("Eres mayor de edad")
    else:
        print("Eres menor de edad")

def ejercicio2():
    
    numeros_lista = input("Ingrese una lista de números separados por comas: ")

    numeros = [float(numero) for numero in numeros_lista.split(',')]


    suma = 0
    for numero in numeros:
        suma += numero

    print("La suma de los elementos es:", suma)

def ejercicio3():
    Razas = ["Beagle", "Fox Hound", "Dalmata", "Setter Irlandes" ]

    nueva_raza=input("Ingresa nueva raza de perro")
    posicion=int(input("Ingresar posicion"))
    Razas.insert(posicion,nueva_raza)
    
    print("Las razas son: ", Razas)

def ejercicio4():
    
    numeros_lista = input("Ingrese una lista de números separados por comas: ")

    numeros = [int(numero) for numero in numeros_lista.split(',')]


    cantidad_pares = 0
    for numero in numeros:
        if numero % 2 == 0:
            cantidad_pares += 1

        print("La cantidad de números pares en la lista es:", cantidad_pares)

def ejercicio5():
    numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))

    print(f"Tabla de multiplicar del {numero}:")
    for factor in range(1, 11):
        resultado = numero * factor
        print(f"{numero} x {factor} = {resultado}")

while True:
    print("Menú de Ejercicios:")
    print("1. Igresar edad y determinar si eres o no mayor de edad.")
    print("2. Ingresar lista de numeros y sumarlos.")
    print("3. Ingresar una nueva raza de perros a la lista")
    print("4. Determinar numeros pares en una lista.")
    print("5. Ingresar un numero para ver su tabla de multiplicar")
    print("0. Salir")
    
    opcion = int(input("Ingrese el número de ejercicio que desea realizar (0 para salir): "))

    if opcion == 1:
        ejercicio1()
    elif opcion == 2:
        ejercicio2()
    elif opcion == 3:
        ejercicio3()
    elif opcion == 4:
        ejercicio4()
    elif opcion == 5:
        ejercicio5()
    elif opcion == 0:
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione un número de ejercicio válido.")

