ARCHIVO_CSV = "/Users/Ivan/curso/paises.csv"

# ==================================
# FUNCIONES AUXILIARES PARTE 1
# ==================================

# Solicita un texto y valida que no esté vacío.
def pedir_texto(mensaje):
    while True:
        texto = input(mensaje).strip()

        if texto != "":
            return texto

        print("Error: el campo no puede estar vacío.")

# Solicita un número entero mayor a cero.
def pedir_entero(mensaje):
    while True:
        dato = input(mensaje).strip()

        if dato == "":
            print("Error: el campo no puede estar vacío.")
        else:
            try:
                numero = int(dato)

                if numero > 0:
                    return numero
                else:
                    print("Error: el número debe ser mayor a cero.")

            except ValueError:
                print("Error: debe ingresar un número entero.")

def mostrar_pais(pais):
    print("-" * 30)
    print(f"  Nombre:      {pais['nombre']}")
    print(f"  Población:   {pais['poblacion']:,}")
    print(f"  Superficie:  {pais['superficie']:,} km²")
    print(f"  Continente:  {pais['continente']}")
    print("-" * 30)


# ==================================
# FUNCIONES AUXILIARES PARTE 2
# ==================================

# Lee el archivo CSV y devuelve una lista de diccionarios con los datos de cada país.
def cargar_paises():
    paises = []
    try:
        with open(ARCHIVO_CSV, "r", encoding="utf-8") as archivo:

            next(archivo)

            for linea in archivo:

                try:
                    nombre, poblacion, superficie, continente = linea.strip().split(",")

                    pais = {
                        "nombre": nombre,
                        "poblacion": int(poblacion),
                        "superficie": int(superficie),
                        "continente": continente.strip()
                    }

                    paises.append(pais)

                except ValueError:
                    print("Error en una linea del CSV.")
                    continue

    except FileNotFoundError:
        print("Error: No se encontro el archivo paises.csv")

    return paises

def mostrar_paises(paises):
    for pais in paises:
        mostrar_pais(pais)


# ==================================
# GUARDAR EN CSV
# ==================================

def guardar_paises(paises):
    with open(ARCHIVO_CSV, "w", encoding="utf-8") as archivo:
        archivo.write("nombre,poblacion,superficie,continente\n")
        for pais in paises:
            archivo.write(f"{pais['nombre']},{pais['poblacion']},{pais['superficie']},{pais['continente']}\n")


# ==================================
# PUNTO 1 - AGREGAR PAÍS
# ==================================

def agregar_pais(paises):

    nombre = pedir_texto("Ingrese el nombre del país: ")

    # Verifica que el país no exista ya en la lista.
    for pais in paises:
        if pais["nombre"].lower() == nombre.lower():
            print("Error: ese país ya existe en la base de datos.")
            return

    poblacion = pedir_entero("Ingrese la población: ")
    superficie = pedir_entero("Ingrese la superficie en km²: ")
    continente = pedir_texto("Ingrese el continente: ")

    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }

    paises.append(nuevo_pais)
    guardar_paises(paises)
    print("\nPaís agregado correctamente.")


# ==================================
# PUNTO 2 - ACTUALIZAR PAÍS
# ==================================

def actualizar_pais(paises):

    if len(paises) == 0:
        print("No hay países cargados para actualizar.")
        return

    nombre_buscado = pedir_texto("Ingrese el nombre exacto del país a actualizar: ").lower()

    encontrado = False

    for pais in paises:

        if pais["nombre"].lower() == nombre_buscado:

            print("\nPaís encontrado:")
            print("Nombre:", pais["nombre"])
            print("Población actual:", pais["poblacion"])
            print("Superficie actual:", pais["superficie"])

            # Solicita los nuevos valores.
            pais["poblacion"] = pedir_entero("Ingrese la nueva población: ")
            pais["superficie"] = pedir_entero("Ingrese la nueva superficie en km²: ")

            encontrado = True
            break

    if encontrado:
        guardar_paises(paises)
        print("\nPaís actualizado correctamente.")
    else:
        print("\nNo se encontró un país con ese nombre.")


# ==================================
# PUNTO 3 - BUSCAR PAÍS
# ==================================

def buscar_pais(paises):

    busqueda = pedir_texto("Ingrese el nombre o parte del nombre del país: ").lower()

    encontrado = False

    for pais in paises:

        # Busca coincidencias parciales o exactas.
        if busqueda in pais["nombre"].lower():
            mostrar_pais(pais)
            encontrado = True

    if not encontrado:
        print("\nNo se encontraron resultados.")


# ==================================
# FILTROS
# ==================================

def filtrar_continente(paises):
    continente = pedir_texto("Ingrese continente: ")

    encontrado = False
    for pais in paises:
        if pais["continente"].lower() == continente.lower():
            mostrar_pais(pais)
            encontrado = True

    if not encontrado:
        print("No existe ese continente en la base de datos.")

def filtrar_poblacion(paises):
    while True:
        try:
            minimo = int(input("Ingrese población minima: "))
            maximo = int(input("Ingrese población maxima: "))

            if minimo < 0 or maximo < 0:
                print("Los valores no pueden ser negativos.")
                continue

            if minimo > maximo:
                print("La población minima no puede ser mayor que la maxima.")
                continue

            break

        except ValueError:
            print("Debe ingresar numeros enteros.")

    encontrado = False
    for pais in paises:
        if minimo <= pais["poblacion"] <= maximo:
            mostrar_pais(pais)
            encontrado = True

    if not encontrado:
        print("No se encontraron paises en ese rango.")

def filtrar_superficie(paises):
    while True:
        try:
            minimo = int(input("Ingrese superficie minima: "))
            maximo = int(input("Ingrese superficie maxima: "))

            if minimo < 0 or maximo < 0:
                print("Los valores no pueden ser negativos.")
                continue

            if minimo > maximo:
                print("La superficie minima no puede ser mayor que la maxima.")
                continue

            break

        except ValueError:
            print("Debe ingresar numeros enteros.")

    encontrado = False
    for pais in paises:
        if minimo <= pais["superficie"] <= maximo:
            mostrar_pais(pais)
            encontrado = True

    if not encontrado:
        print("No se encontraron paises en ese rango.")


# ==================================
# ORDENAMIENTOS
# ==================================

def ordenar_nombre(paises):

    auxiliar = paises.copy() #Creo una copia de la lista de paises

    for i in range(len(auxiliar)-1):

        for j in range(i+1, len(auxiliar)):

            if auxiliar[i]["nombre"] > auxiliar[j]["nombre"]:
                temp = auxiliar[i]
                auxiliar[i] = auxiliar[j]
                auxiliar[j] = temp
    return auxiliar

def ordenar_poblacion(paises):

    auxiliar = paises.copy()

    for i in range(len(auxiliar)-1):

        for j in range(i+1, len(auxiliar)):

            if auxiliar[i]["poblacion"] > auxiliar[j]["poblacion"]:

                temp = auxiliar[i]
                auxiliar[i] = auxiliar[j]
                auxiliar[j] = temp

    return auxiliar

def ordenar_superficie_asc(paises):

    auxiliar = paises.copy()

    for i in range(len(auxiliar)-1):

        for j in range(i+1, len(auxiliar)):

            if auxiliar[i]["superficie"] > auxiliar[j]["superficie"]:

                temp = auxiliar[i]
                auxiliar[i] = auxiliar[j]
                auxiliar[j] = temp

    return auxiliar

def ordenar_superficie_des(paises):

    auxiliar = paises.copy()

    for i in range(len(auxiliar)-1):

        for j in range(i+1, len(auxiliar)):

            if auxiliar[i]["superficie"] < auxiliar[j]["superficie"]:

                temp = auxiliar[i]
                auxiliar[i] = auxiliar[j]
                auxiliar[j] = temp

    return auxiliar


# ==================================
# ESTADÍSTICAS
# ==================================

def pais_menor_poblacion(paises):
    menor = paises[0]
    for pais in paises:
        if(pais["poblacion"]< menor["poblacion"]):
            menor=pais
    print("Pais con menor poblacion:")
    mostrar_pais(menor)

def pais_mayor_poblacion(paises):
    mayor = paises[0]
    for pais in paises:
        if(pais["poblacion"]>mayor["poblacion"]):
            mayor = pais
    print("Pais con mayor poblacion:")
    mostrar_pais(mayor)

def promedio_poblacion(paises):

    suma = 0

    for pais in paises:
        suma += pais["poblacion"]

    promedio = suma / len(paises)

    print("Promedio de poblacion:", promedio)

def promedio_superficie(paises):

    suma = 0

    for pais in paises:
        suma += pais["superficie"]

    promedio = suma / len(paises)

    print("Promedio de superficie:", promedio)

def cantidad_paises_por_continente(paises):
    america = 0
    europa = 0
    asia = 0
    africa = 0
    oceania = 0

    for pais in paises:

        if pais["continente"] == "América":
            america += 1

        elif pais["continente"] == "Europa":
            europa += 1

        elif pais["continente"] == "Asia":
            asia += 1

        elif pais["continente"] == "África":
            africa += 1

        elif pais["continente"] == "Oceanía":
            oceania += 1

    print("Cantidad de países por continente:")
    print("América:", america)
    print("Europa:", europa)
    print("Asia:", asia)
    print("África:", africa)
    print("Oceanía:", oceania)

def mostrar_estadisticas(paises):
    if not paises:
        print("No hay países cargados.")
        return
    print("\n===== ESTADÍSTICAS =====")
    pais_mayor_poblacion(paises)
    pais_menor_poblacion(paises)
    promedio_poblacion(paises)
    promedio_superficie(paises)
    cantidad_paises_por_continente(paises)


# ==================================
# MENÚ PRINCIPAL
# ==================================

def mostrar_menu():

    print("\n===== GESTIÓN DE PAÍSES =====")
    print("1.  Mostrar países")
    print("2.  Agregar un país")
    print("3.  Actualizar un país")
    print("4.  Buscar por nombre")
    print("5.  Filtrar por continente")
    print("6.  Filtrar por rango de población")
    print("7.  Filtrar por rango de superficie")
    print("8.  Ordenar por nombre")
    print("9.  Ordenar por población")
    print("10. Ordenar por superficie ascendente")
    print("11. Ordenar por superficie descendente")
    print("12. Mostrar estadísticas")
    print("0.  Salir")

    opcion = input("Ingrese una opción: ")

    return opcion

def main():
    paises = cargar_paises()

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
            mostrar_paises(paises)

        elif opcion == "2":
            agregar_pais(paises)

        elif opcion == "3":
            actualizar_pais(paises)

        elif opcion == "4":
            buscar_pais(paises)

        elif opcion == "5":
            filtrar_continente(paises)

        elif opcion == "6":
            filtrar_poblacion(paises)

        elif opcion == "7":
            filtrar_superficie(paises)

        elif opcion == "8":
            listaOrdenada = ordenar_nombre(paises)
            mostrar_paises(listaOrdenada)

        elif opcion == "9":
            listaOrdenada = ordenar_poblacion(paises)
            mostrar_paises(listaOrdenada)

        elif opcion == "10":
            listaOrdenada = ordenar_superficie_asc(paises)
            mostrar_paises(listaOrdenada)

        elif opcion == "11":
            listaOrdenada = ordenar_superficie_des(paises)
            mostrar_paises(listaOrdenada)

        elif opcion == "12":
            mostrar_estadisticas(paises)

        elif opcion == "0":
            print("Programa finalizado.")
            break

        else:
            print("Opción inválida.")

main()
