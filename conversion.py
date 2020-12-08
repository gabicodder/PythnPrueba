
def convertir(pesos,moneda):
    cambio = 0
    try:
        if moneda == 1:
            cambio = pesos/745
            return print(f'\n:::::> La conversión de {pesos} pesos CLP a USD es {round(cambio,2)} USD\n')
        else:
            cambio = pesos/905
            return print(f'\n:::::> La conversión de {pesos} pesos CLP a EUR es {round(cambio,2)} EUR\n')
    except Exception:
        print('\n!¡!¡!:::::::::::Ingrese un valor correcto::::::::::::::!¡!¡!¡\n')


def run():
    """"""""
    print(':::::Conversion A USD y EUR::::::::\n')
    while True:
        try:
            print('1. Convertir a USD\n'+
                '2. Convertir a EUR\n'+
                '3. Salir\n')
            opcion = int(input('::> Elija una Opcion: '))

            if opcion > 0 and opcion <= 2:
                pesos = float(input('Ingresa la cantidad en pesos: '))
                if pesos < 0:
                    print(':::::::Ha ingresado una cantidad negativa\n::::::::::::\n')
                    pesos = float(input('Ingresa la cantidad en pesos: '))

                convertir(pesos,opcion)

            elif opcion == 3:
                break;
            else:
                print('\n!!!!:::::Ingrese una opción correcta::::::!!!!!\n')

        except Exception:
            print('\n!!!!:::::Ingrese solo numeros::::::!!!!!\n')


if __name__ == "__main__":
    run()