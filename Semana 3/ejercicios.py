# Vamos a crear un programa en python donde vamos a declarar 
# un diccionario para guardar los precios de las distintas frutas.
# El programa pedirá el nombre de la fruta y la cantidad que se ha
# vendido y nos mostrará el precio final de la fruta a partir
# de los datos guardados en el diccionario. Si la fruta no existe
# nos dará un error. Tras cada consulta el programa nos preguntará si 
# queremos hacer otra consulta.

dict = {
    "pera"      : 2.30,
    "manzana"   : 1.50,
    "platano"   : 1.80,
    "piña"      : 5.00,
    "mandarina" : 3.20,
    "naranja"   : 4.10,
    "tomate"    : 2.50
}

def pedirNombre():
    nombre = input('Ingrese el nombre de la fruta a buscar: ')
    nombre = nombre.lower()
    return nombre

def pedirCantidad():
    cantidad = int(input('Ingrese la cantidad vendida: '))
    return cantidad

def consulta(dict, nombre):
    lista = dict.keys()
    if nombre in lista:
        precio = dict.get(nombre)
    else:
        return -1
    return precio

print(dict)
while True:
    print()
    nombre = pedirNombre()
    cantidad = pedirCantidad()
    precio = consulta(dict, nombre)
    if precio != -1:
        print(f'El precio final de {nombre} es {precio * cantidad}')
    else:
        print('Error...')
    rpta = input('Una fruta mas? Si/No')
    rpta = rpta.lower()
    if rpta == 'no':
        print('Hablamos!')
        break