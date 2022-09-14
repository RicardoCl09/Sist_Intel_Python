def ingresoDatos():
    while True:
        sexo = str(input("Ingresar sexo(m/f): "))
        if(sexo.lower() == 'm' or sexo.lower() == 'f'):
            break
        else:
            print("Opcion invalida. Vuelve a intentar.")
            continue
    while True:
        edad = int(input("Ingresar edad: "))
        if(edad < 0 or edad > 99):
            print("Ingrese una edad valida.")
            continue
        else:
            break
    return sexo,edad

def montoTotal(sexo,edad):
    if sexo == 'm':
        if edad < 25:
            print('Debe pagar 1000 soles.')
        else:
            print('Debe pagar 700 soles.')
    else:
        if edad < 21:
            print('Debe pagar 800 soles.')
        else:
            print('Debe pagar 500 soles.')
    
def reporte(sexo,edad):
    montoTotal(sexo,edad)

sexo,edad = ingresoDatos()
reporte(sexo, edad)