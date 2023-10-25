# Funcion para crear números
def sumar_dos():
    # Iniciando un bucle
    while True:
        # Pide números
        a = input("Número 1: ")
        b = input("Número 1: ")

        # intentado convertir a entero y sumarlos
        try:
            resultado = int(a) + int(b)

        # Si lanzo una excepción, pedirle que reingrese los datos
        except ValueError as e:
            print('Te pedi números salame, no te hagas el gracioso')
            print(f'EROORRR!! {e}')
        # si to-do sale bien terminamos el bucle
        else:
            break
        finally:
            print('Esto se ejecuta siempre')
    return resultado

print(sumar_dos())
