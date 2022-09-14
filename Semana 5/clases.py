from math import pi

# Ejercicio 1
class TrianguloRectangulo:
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2
    
    def Area(self):
        return self.cateto1 * self.cateto2 / 2
    
    def Hipotenusa(self):
        return ((self.cateto1) ** 2 + (self.cateto2) ** 2) ** 0.5
    
    def Perimetro(self):
        return self.cateto1 + self.cateto2 + self.Hipotenusa()
    
# Ejercicio 2
class ConversionTemperatura:
    def __init__(self, celsius):
        self.celsius = celsius
    
    def converFahrenheit(self):
        return (self.celsius * 9 / 5) + 32
    
# Ejercicio 3
class Producto:
    def __init__(self, nombre, costo, venta):
        self.nombre = nombre
        self.precioCosto = costo
        self.precioVenta = venta
    
    def ganancia(self):
        return self.precioVenta - self.precioCosto
    
# Ejercicio 4
class Trabajador:
    def __init__(self, nombre, precioHora, horasTrabajadas):
        self.nombre = nombre
        self.precioHora = precioHora
        self.horasTrabajadas = horasTrabajadas
    
    def salarioBruto(self):
        return self.precioHora * self.horasTrabajadas
    
    def impuesto(self):
        return self.salarioBruto() * 0.1
    
    def salarioNeto(self):
        return self.salarioBruto() - self.impuesto()
    
# Ejercicio 5
class Movil:
    def __init__(self, velocidadInicial, tiempo, aceleracion):
        self.velocidadInicial = velocidadInicial
        self.tiempo = tiempo
        self.aceleracion = aceleracion
    
    def distaciaRecorrida(self):
        return (self.velocidadInicial * self.tiempo) + (self.aceleracion * 0.5 * self.tiempo ** 2)
    
# Ejercicio 6
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Caja(Rectangulo):
    def __init__(self, base, altura, profundidad):
        Rectangulo.__init__(self, base, altura)
        self.profundidad = profundidad
    
    def volumen(self):
        return self.area() * self.profundidad
    
# Ejercicio 7
class ObjetoGeometrico:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def distanciaOrigen(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

class Circulo(ObjetoGeometrico):
    def __init__(self, x, y):
        super().__init__(x, y)
    
    def area(self):
        return pi * self.distanciaOrigen() ** 2

class Cuadrado(ObjetoGeometrico):
    def __init__(self, x, y):
        super().__init__(x, y)
        
    def area(self):
        return (self.distanciaOrigen() * 2) ** 2