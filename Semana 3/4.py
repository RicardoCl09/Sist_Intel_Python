# Codifica un programa en python que nos permita guardar los nombres de los alumnos de una clase y las
# notas que han obtenido. Cada alumno puede tener distinta cantidad de notas. Guarda la información en
# un diccionario cuya claves serán los nombres de los alumnos y los valores serán listas con las notas de
# cada alumno.
# El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus
# notas hasta que introduzcamos un número negativo. Al final el programa nos mostrará la lista
# de alumnos y la nota media obtenida por cada uno de ellos. Nota: si se introduce el nombre de un alumno que ya
# existe el programa nos dará un error.

def crearNotas():
    i = 1
    lista = []
    while True:
        nota = float(input(f'Ingrese nota {i}: '))
        if nota <= -1 or nota >= 21:
            break
        lista.append(nota)
        i += 1
    return lista

def alumnos():
    numero = int(input('Ingrese numero de alumnos: '))
    dict = {}
    for i in range(numero):
        nombre = input(f'Ingrese nombre de alumno {i + 1}: ')
        if nombre in dict:
            print('ERROR...')
            break
        else:
            lista = crearNotas()
            dict[nombre] = lista
    return dict

def calculoPromedio(dict):
    promedio = {}
    for e in dict: 
        lista = dict[e]
        suma = 0
        for i in lista:
            suma += i
        suma /= len(lista)
        promedio[e] = suma
    return promedio


alumnos = alumnos()
for i in alumnos:
    print(i, ': ', alumnos[i])
promedios = calculoPromedio(alumnos)
print('Promedios!!...')
for i in promedios:
    print(i, ': ', promedios[i])
