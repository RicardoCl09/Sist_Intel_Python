#Ejercicio 1
# A = int(input("Ingrese numero A: "))
# B = int(input("Ingrese numero B: "))
# if A % B == 0:
#     print(f'El numero {A} es divisible por el numero {B}')
# else:
#     print(f'El numero {A} no es divisible por el numero {B}')


#Ejercicio 2
# capital = float(input("Ingrese el capital: "))
# if capital < 500:
#     interes = 2
# elif capital >= 500 and capital <= 1500:
#     interes = 4.5
# elif capital > 1500:
#     interes = 9
# print("La tasa de interes será: ", interes)


#Ejercicio 3
# a = int(input("Primer numero: "))
# b = int(input("Segundo numero: "))
# c = int(input("Tercer numero: "))
# if a >= b:
#     if a >= c:
#         if c >= b:
#             print("El numero intermedio es: ", c)
#         else:
#             print("El numero intermedio es: ", b)
#     else:
#         print("El numero intermedio es: ", a)
# elif b >= a:
#     if b >= c:
#         if c >= a:
#             print("El numero intermedio es ", c)
#         else:
#             print("El numero intermedio es: ", a)
#     else:
#         print("El numero intermedio es: ", b)


#Ejercicio 4
# letra = input("Ingrese una letra: ")
# if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
#     print("La letra es una vocal")
# elif letra == 'y':
#     print("La letra es una semivocal")
# else:
#     print("La letra es una consonante")


#Ejercicio 5
# mes = int(input("Ingrese el numero de mes: "))
# if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
#     print("El numero de dias es 31")
# elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
#     print("El numero de dias es 30")
# else:
#     print("El numero de dias es 28 o 29")


#Ejercicio 6
# propina = 100
# informatica = int(input("Ingrese nota de informatica: "))
# calculo = int(input("Ingrese nota de calculo: "))
# fisica = int(input("Ingrese nota de fisica: "))
# if informatica >= 12:
#     propina = propina + 20
# if calculo >= 12:
#     propina = propina + 20
# if fisica >= 12:
#     propina = propina + 20
# print("Propina final: ", propina)

#Ejercicio 7
# variante = float(input("Ingrese valor de x: "))
# if variante >= 0:
#     resultado = 4 * variante ** 2 - 2
# else:
#     resultado = variante ** 3 + variante / 2
# print("El valor de F(x) es: ", resultado)


#Ejercicio 8
# x = int(input("Ingrese valor de lado x: "))
# y = int(input("Ingrese valor de lado y: "))
# z = int(input("Ingrese valor de lado z: "))
# if x > 0 and y > 0 and z > 0:
#     if x + y > z and x + z > y and y + z > x:
#         print("Se forma un triangulo ", end = " ")
#     if x == y and y == z:
#         print("Equilátero.")
#     elif x == y or x == z or y == z:
#         print("isósceles.")
#     else:
#         print("Escaleno.")
# else:
#     print("No se forma un triangulo.")


#Ejercicio 9
# numero = int(input("Ingrese numero de 4 digitos: "))
# u = numero % 10
# d = (numero % 100) // 10
# c = (numero % 1000) // 100
# m = numero // 1000
# if m % 2 == 0 and c % 2 == 0 and d % 2 == 0 and u % 2 == 0:
#     print("Todos los digitos son pares")
# else:
#     print("Existe al menos un digito impar")

#Ejercicio 10
# nota1 = int(input("Ingrese nota 1: "))
# nota2 = int(input("Ingrese nota 2: "))
# nota3 = int(input("Ingrese nota 3: "))
# nota4 = int(input("Ingrese nota 4: "))
# # notas = [nota1, nota2, nota3 ,nota4]
# # print(min(notas))
# menor = nota1
# if nota2 < menor:
#     menor = nota2
# if nota3 < menor:
#     menor = nota3
# if nota4 < menor:
#     menor = nota4
# if nota1 == menor:
#     promedio = (nota2 + nota3 + nota4) / 3
# elif nota2 == menor:
#     promedio = (nota1 + nota3 + nota4) / 3
# elif nota3 == menor:
#     promedio = (nota1 + nota2 + nota4) / 3
# elif nota4 == menor:
#     promedio = (nota1 + nota2 + nota3) / 3
# print("La menor nota es ", menor)
# print("El promedio es: ", promedio)


#Ejercicio 11
# monto = int(input("Ingrese monto total vendido: "))
# if monto > 5000:
#     extra = ((monto - 5000) // 500) * 25
#     sueldo = monto + extra
# else:
#     sueldo = monto
# print("El sueldo final del trabajador es: ", sueldo)


#Ejercicio 12
# numero = int(input("Ingrese numero de 3 cifras: "))
# u = numero % 10
# d = (numero % 100) // 10
# c = numero // 100
# conversion = u * 100 + d * 10 + c
# if conversion == numero:
#     print("El numero es capicua.")
# else:
#     print("El numero no es capicua.")


#Ejercicio 13
peso = float(input("Ingrese peso: "))
estatura = float(input("Ingrese estatura: "))
imc = peso / estatura ** 2
print("Grado de Obesidad: ")
if imc < 20:
    print("Delgado")
elif imc >= 20 and imc < 25:
    print("Normal")
elif imc >= 25 and imc < 27:
    print("Sobrepeso")
else:
    print("Obesidad")
