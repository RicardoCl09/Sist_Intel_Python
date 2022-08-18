#Ejercicio 1 

# a = float(input('Ingrese primer numero: '))
# b = float(input('Ingrese segundo numero: '))
# print('La suma es: ', a + b)
# print('La resta es: ', a - b)
# print('El producto es: ', a * b)


#Ejercicio 2

# G = 9.8
# T = float(input('Ingresar el tiempo recorrido en segundos: '))
# H = 0.5 * G * T ** 2
# print('La altura de la que cae es: ', H)


#Ejercicio 3

# import math

# altura = float(input('Ingrese la altura del cilindro: '))
# radio = 2
# volumen = math.pi * radio ** 2 * altura
# print('El volumen del cilindro es: ', volumen)


#Ejercicio 4

# basico = 300 
# monto = float(input('Ingresar monto vendido: '))
# comision = 0.9 * monto
# bruto = basico + comision
# descuento = bruto * 0.11
# neto = bruto - descuento
# print('La comision es: ', comision)
# print('El sueldo bruto es: ', bruto)
# print('El descuento es: ', descuento)
# print('El sueldo neto es: ', neto)


#Ejercicio 5

# x1, x2 = int(input('El punto x1 es: ')), int(input('El punto x2 es: '))
# print(f'Primer punto: ({x1}, {x2})')

# y1, y2 = int(input('El punto y1 es: ')), int(input('El punto y2 es: '))
# print(f'Segundo punto: ({y1}, {y2})')

# distancia1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
# distancia2 = pow( pow(x2 - x1, 2) + pow(y2 - y1, 2) , 0.5)
# print('La distancia entre los dos puntos es: ',  distancia1, distancia2)


#Ejercicio 6

# cantidad = int(input('La cantidad de dinero es: '))
# if cantidad / 100 > 0:
#     cambio = int(cantidad / 100)
#     cantidad = cantidad % 100
#     print('Billetes de 100 soles: ', cambio)
# if(cantidad / 50 > 0):
#     cambio = int(cantidad / 50)
#     cantidad = cantidad % 50
#     print('Billetes de 50:', cambio)
# if(cantidad / 10 > 0):
#     cambio = int(cantidad / 10)
#     cantidad = cantidad % 10
#     print('Billetes de 10: ', cambio)
# if(cantidad / 5 > 0):
#     cambio = int(cantidad / 5)
#     cantidad = cantidad % 5
#     print('Monedas de 5:', cambio)
# if(cantidad / 2 > 0):
#     cambio = int(cantidad / 2)
#     cantidad = cantidad % 2
#     print('Monedas de 2: ', cambio)
# print('Monedas de 1: ', cantidad)


#Ejercicio 7
# a = int(input("Ingrese numero: "))
# if a < 1000:
#     conversion = int(str(a)[len(str(a)) - 1])
# else:
#     conversion = int(str(a)[len(str(a)) - 4] + str(a)[len(str(a)) - 1])
# print("Conversion: ", conversion)

# numero = int(input("Ingrese numero: "))
# u = numero % 10
# m = numero // 100
# r = m * 10 + u
# print(r)


#Ejercicio 8
# numero = int(input(""))
# i = int(len(str(numero)))
# conversion = ""
# while i > 0:
#     conversion = conversion + str(numero)[i - 1]
#     i = i - 1
# print("Numero invertido: ", conversion)

# numero = int(input("Ingresar numero: "))
# u = numero % 10
# d = (numero % 100) // 10
# c = numero // 100
# conversion = u * 100 + d * 10 + c
# print("Numero invertido: ", conversion)


#Ejercicio 9
# precioLitros = 3.86
# galones = int(input("Numero de galones vendidos: "))
# cobro = galones * 3.785 * precioLitros
# print("Total a cobrar: ", cobro)

#Ejercicio 10
capital = float(input("Ingrese el capital: "))
periodos = int(input("Ingrese el numero de periodos: "))
interes = float(input("Ingrese tasa de interes: "))
monto = capital * (1 + interes/100) ** periodos
interes = monto - capital
print("Interes generado: ", capital)