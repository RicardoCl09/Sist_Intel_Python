# Numero maximo de vendedores: 30
# Numero de minutos fijos: 20 minutos
# Extra: 0.35 por minuto

# Numero de minutos celulares: 40 minutos
# Extra: 0.45 por minuto

# Numero de mensajes: 20 mensajes.
# Extra: 0.20 por mensaje

def numVendedores():
    while True:
        n = int(input('Ingrese numero de vendedores: '))
        if n > 0 and n < 31:
            break
        print('Vendedores debe estar entre 0 y 30')
    return n

def crearDictTarifas():
    tarifas = {}
    dato = int(input('Ingrese minutos a fijo consumidos: '))
    tarifas['fijo'] = dato
    dato = int(input('Ingrese minutos a celular consumidos: '))
    tarifas['celular'] = dato
    dato = int(input('Ingrese mensajes consumidos: '))
    tarifas['mensajes'] = dato
    return tarifas

def crearDictVendedores(n):
    vendedores = {}
    for i in range(n):
        print(f'Vendedor {i + 1}')
        tarifas = crearDictTarifas()
        vendedores[i + 1] = tarifas
    return vendedores

def codigos_mayor_cantidad_minutos(vendedores):
    mayor = -20
    for vendedor in vendedores:
        if vendedores[vendedor]['celular'] >= mayor:
            mayor = vendedores[vendedor]['celular']
    lista = []
    for vendedor in vendedores:
        if vendedores[vendedor]['celular'] == mayor:
            lista.append(vendedor)
    return lista

def reporteMayorConsumo(lista):
    print('Los mayores consumidores fueron...')
    for i in lista:
        print(f'Vendedor {i}')

def total_pagar_x_vendedor(vendedores):
    for vendedor in vendedores: 
        fijos = (vendedores[vendedor]['fijo'] - 20) * 0.35
        celulares = (vendedores[vendedor]['celular'] - 40) * 0.45
        mensajes = (vendedores[vendedor]['mensajes'] - 20) * 0.2
        total = fijos + celulares + mensajes
        if total > 0:
            print(f'El pago por exceso del vendedor {vendedor} es: {total} soles')
        else:
            print(f'El vendedor {vendedor} no tiene exceso.')

def tiempo_promedio(n, vendedores):
    fijos = 0
    celulares = 0
    mensajes = 0
    for vendedor in vendedores: 
        fijos += vendedores[vendedor]['fijo']
        celulares += vendedores[vendedor]['celular']
        mensajes += vendedores[vendedor]['mensajes']
    return  fijos / n, celulares / n, mensajes / n

def reportePromedios(promFijos, promCel, promMen):
    print(f'El promedio de minutos a telefonos fijos es: {promFijos}')
    print(f'El promedio de minutos a celulares es: {promCel}')
    print(f'El promedio de mensajes de texto es: {promMen}')

n = numVendedores()
vendedores = crearDictVendedores(n)
print()
print('Diccionario de vendedores')
print(vendedores)
print()
print()
print('Codigos de mayores consumidores de minutos a celular....')
lista = codigos_mayor_cantidad_minutos(vendedores)
reporteMayorConsumo(lista)
print()
print()
print('Exceso de vendedores....')
total_pagar_x_vendedor(vendedores)
print()
print()
print('Promedios de consumo....')
promFijos, promCel, promMen = tiempo_promedio(n, vendedores)
reportePromedios(promFijos, promCel, promMen)

