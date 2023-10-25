# 2 listas, una con nombres, otra con apellidos
nombres = ['Nicolas', 'Pedri', 'Jude', 'Cristiano', 'David']
apellidos = ['Gutierrez', 'Gonzalez', 'Bellingham', 'Dos Santos', 'Beckham']

# Registrar esta información en un TXT de forma óptima
try:
    with open('nombres_y_apellidos.txt', 'w') as file:

        file.writelines('Los datos son: \n\n')
        [file.writelines(f'Nombre: {n} \nApellido: {a}\n--------------\n') for n, a in zip(nombres, apellidos)]
        print('Con exito :)')
except:
    print('Sin Exito :c')
