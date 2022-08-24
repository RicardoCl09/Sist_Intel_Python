# Ejercicio 1
# lista = []
# n = int(input('Numero de elementos de la lista: '))
# for i in range(1, n + 1):
#     numero = int(input('Ingrese numero: '))
#     lista.append(numero)
    
# listaPares = [x for x in lista if x % 2 == 0]
# listaNegativos = [x for x in lista if x < 0]

# print('Lista de pares: ', listaPares)
# print('Lista negativos: ', listaNegativos) 

# Ejercicio 2
# listaC = []
# listaA = []
# listaB = []
# nA = int(input('Ingrese numero de elementos de A: '))
# nB = int(input('Ingrese numero de elementos de B: '))

# print('Lista A...')
# for i in range(0, nA):
#     numero = int(input(f'Ingrese elemento {i}: '))
#     listaA.append(numero)
    
# print('Lista B...')
# for i in range(0, nB):
#     numero = int(input(f'Ingrese elemento {i}: '))
#     listaB.append(numero)

# for i in range(0, max(nA, nB)):
#     if nA >= nB:
#         if i >= nB:
#             listaC.append(listaA[i])
#         else:
#             listaC.append(listaA[i] + listaB[i])
#     else:
#         if i >= nA:
#             listaC.append(listaB[i])
#         else:
#             listaC.append(listaA[i] + listaB[i])

# print(listaA)
# print(listaB)
# print(listaC)

# Ejercicio 3
# n = int(input('Ingrese numero de datos: '))
# lista = []
# acumulado = 0
# for i in range(0, n):
#     numero = int(input(f'Ingrese dato {i}: '))
#     lista.append(numero)

# for elem in lista:
#     acumulado += 1 / elem

# armonica = len(lista) / acumulado
# print('La media armónica es: ', armonica)


# Ejercicio 4
# n = int(input('Ingrese numero de elementos: '))
# lista = []
# for i in range (n):
#     numero = float(input(f'Ingrese elemento {i}: '))
#     lista.append(numero)

# promedio = 0
# for e in lista: 
#     promedio += e

# promedio /= n
# print('Numeros menores al promedio: ', end=' ')
# for e in lista:
#     if e < promedio:
#         print(e, end=', ')


# Ejercicio 5
# n = int(input('Ingrese numero de notas: '))
# lista = []
# for i in range(n):
#     nota = float(input(f'Ingrese nota {i + 1}: '))
#     lista.append(nota)

# contador = 0
# for e in lista:
#     if e < 12:
#         contador += 1

# desaprobados = contador * 100 / n
# aprobados = 100 - desaprobados
# print(f'El porcentaje de aprobados es {aprobados}%')
# print(f'El porcentaje de desaprobados es {desaprobados}%')


# Ejercicio 6
# n = int(input('Ingrese numero de elementos: '))
# lista = []
# for i in range(n):
#     elemento = input(f'Ingrese elemento {i}: ')
#     lista.append(elemento)
    
# contador = 0
# buscado = input('Ingrese elemento a buscar: ')
# for e in lista:
#     if buscado == e:
#         contador += 1

# print(f'El numero de veces que aparece {buscado} en lista es: {contador}')


# Ejercicio 7
# lista1 = [1, 2, 3, 4, 5]
# lista2 = [1, 2, 3, 4]
# if lista1 == lista2:
#     print('Las listas son iguales.')
# else:
#     print('Las listas no son iguales.')


# Ejercicio 8
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# if len(lista) % 2 == 0:
#     mediana = (lista[len(lista) // 2] + lista[len(lista) // 2 - 1]) / 2
# else:
#     mediana = lista[len(lista) // 2]

# print(f'La mediana es: {mediana}')

# n = int(input('Ingrese numero de datos: '))
# lista = []
# for i in range(n):
#     dato = float(input(f'Ingrese dato {i}: '))
#     lista.append(dato)

# lista.sort()
# print(lista)
# if n % 2 == 0:
#     mediana = (lista[n // 2] + lista[n // 2 - 1]) / 2
# else:
#     mediana = lista[n // 2]
    
# print(f'La mediana es: {mediana}')


# Ejercicio 9
n = int(input('Ingrese numero de datos lista 1: '))
lista1 = []
for i in range(n):
    dato = input(f'Ingrese dato {i}: ')
    lista1.append(dato)
    
i = 0
while i < len(lista1):
    j = i + 1
    while j < len(lista1):
        if lista1[i] == lista1[j]:
            del lista1[j]
            j = j - 1
        j = j + 1
    i = i + 1

lista2 = []
m = int(input('Ingrese numero de datos lista 2: '))
for i in range(m):
    dato = input(f'Ingrese dato {i}: ')
    lista2.append(dato)
    
i = 0
while i < len(lista2):
    j = i + 1
    while j < len(lista2):
        if lista2[i] == lista2[j]:
            del lista2[j]
            j = j - 1
        j = j + 1
    i = i + 1
    

union = lista1
for elemento in lista2:
    if elemento not in union:
        union.append(elemento)

interseccion = []
for elemento in lista1:
    if elemento in lista2:
        interseccion.append(elemento)


diferencia = []
for elemento in lista1:
    if elemento not in lista2:
        diferencia.append(elemento)
        
union.sort()
interseccion.sort()
diferencia.sort()
print()
print('Lista 1: ', lista1)
print('Lista 2: ', lista2)
print()
print('Union: ', union)
print('Interseccion: ', interseccion)
print('Diferencia: ', diferencia)

# union = []
# if n > m:
#     for i in range(n):
#         if lista1[i] not in union:
#             union.append(lista1[i])
#         if i < len(lista2):
#             if lista2[i] not in union:
#                 union.append(lista2[i])
# else:
#     for i in range(m):
#         if lista2[i] not in union:
#             union.append(lista2[i])
#         if i < len(lista1):
#             if lista1[i] not in union:
#                 union.append(lista1[i])
# print(union)
# diferencia = set(lista1).difference(set(lista2))
# if len(diferencia) > 0 :
#     print(diferencia)