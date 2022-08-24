# Ejercicio 1
# sumaPares = 0
# sumaImpares = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         sumaPares += i
#     else:
#         sumaImpares += i
# print('La suma de los pares es: ', sumaPares)
# print('La suma de los impares es: ', sumaImpares)


# Ejercicio 2
# esNumero = False
# while not esNumero:
#     numero = int(input('Ingrese numero: '))
#     if numero >= 0:
#         esNumero = True
#     else:
#         print('El numero debe ser mayor o igual a 0')

# factorial = 1
# print(f'El factorial de {numero} es:', end = ' ')
# if numero != 0:
#     while numero >= 1:
#         factorial *= numero
#         numero -= 1

# print(factorial)


# Ejercicio 3
# esPositivo = False
# while not esPositivo:
#     n = int(input('¿Ingrese cantidad de numeros?: '))
#     if n <= 0:
#         print('El numero ingresado debe ser mayor a 0')
#     else:
#         esPositivo = True

# promedio = 0
# for i in range(1, n + 1):
#     numero = int(input(f'Ingrese numero #{i}: '))
#     promedio += numero

# promedio /= n
# print('El promedio de los numeros es: ', promedio)


# Ejercicio 4
# numero = int(input('Ingrese numero: '))
# print(numero, end = ' ')
# while numero != 1:
#     if numero % 2 == 0:
#         numero //= 2
#     else:
#         numero *= 3
#         numero += 1
#     print(numero, end = ' ')


# Ejercicio 5
suma = 1
n = int(input('Ingrese n: '))
for i in range(1, n + 1):
    x = int(input(f'Ingrese X{i}: '))
    if i == 1:
        suma += x
    else:
        factorial = 1
        for j in range(1, i + 1):
            factorial *= j
        suma += x / (factorial)
print('La sumatoria es: ', suma)