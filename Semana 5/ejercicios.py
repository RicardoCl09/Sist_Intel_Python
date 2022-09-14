from clases import *

# Ejercicio 1
triangulo = TrianguloRectangulo(3, 4)
print('-----------------------------------')
print('Ejercicio 1 - Triangulo')
print(triangulo.Area())
print(triangulo.Hipotenusa())
print(triangulo.Perimetro())
print('-----------------------------------')

# Ejercicio 2
print('Ejercicio 2 - Conversor Temperatura')
conversor = ConversionTemperatura(28)
print(conversor.converFahrenheit())
print('-----------------------------------')

# Ejercicio 3
print('Ejercicio 3 - Ganancia Producto')
producto = Producto('Leche', 3.50, 5.50)
print(f'La ganancia por la venta de {producto.nombre} es {producto.ganancia()} por unidad')
print('-----------------------------------')

# Ejercicio 4
print('Ejercicio 4 - Salario Trabajador')
trabajador = Trabajador('Marciano', 28.5, 8)
print(f'El salario bruto de {trabajador.nombre} es {trabajador.salarioBruto()}')
print(f'El impuesto de {trabajador.nombre} es {trabajador.impuesto()}')
print(f'El salario neto de {trabajador.nombre} es {trabajador.salarioNeto()}')
print('-----------------------------------')

# Ejercicio 5
print('Ejercicio 5 - Distancia Movil')
movil = Movil(5, 3, 2)
print(f'La distancia recorrida por el movil es {movil.distaciaRecorrida()}')
print('-----------------------------------')

# Ejercicio 6
print('Ejercicio 6 - Rectangulo a Caja')
rectangulo = Rectangulo(3, 4)
caja = Caja(3, 4, 5)
print(f'El area del rectangulo es {rectangulo.area()}')
print(f'El volumen del caja es {caja.volumen()}')
print('-----------------------------------')

# Ejercicio 7
print('Ejercicio 7 - Objeto Geometrico')
objeto = ObjetoGeometrico(1, 1)
circulo = Circulo(1, 1)
cuadrado = Cuadrado(1, 1)
print(f'El centro del objeto es ({objeto.x}, {objeto.y})')
print(f'El area del circulo con centro en ({circulo.x}, {circulo.y}) es {circulo.area()}')
print(f'El area del cuadrado con centro en ({cuadrado.x}, {cuadrado.y}) es {cuadrado.area()}')
print('-----------------------------------')