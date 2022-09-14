def ingresoMensaje():
    cadena = input('Ingrese cadena: ')
    return cadena

def costos(cadena):
    costo = 0
    for i in cadena:
        if i == 'á' or i == 'é' or i == 'í' or i == 'ó' or i == 'ú' or i == 'ñ':
            costo += 30
        if i >= chr(48) and i <= chr(57):
            costo += 20
        if i.lower() >= chr(97) and i.lower() <= chr(122): 
            costo += 10
        if i == " ":
            costo += 0
    return costo

def reporteCosto(costo):
    print(f'El costo de la cadena es: {costo}')
    

cadena = ingresoMensaje()
costo = costos(cadena)
reporteCosto(costo)