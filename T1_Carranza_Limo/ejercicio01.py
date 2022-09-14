def numeroEntradas():
    while True:
        n = int(input('Ingrese la cantidad de entradas a comprar')) 
        if n <= 0 or n >= 5:
            print('Hay un maximo de 4 entradas... Ingrese nuevamente') 
            continue
        return n

def pagoTotal(n):
    precio = float(input('Ingrese precio de la entrada: '))
    if n == 1:
        total = precio * n
    if n == 2:
        total = precio * 0.9 * n
    if n == 3:
        total = precio * 0.85 * n
    if n == 4:    
        total = precio * 0.8 * n
    return total

def reportes(n):
    precioFinal = pagoTotal(n)
    print(f'El pago total a realizar es: {precioFinal}')
    

n = numeroEntradas()
reportes(n)