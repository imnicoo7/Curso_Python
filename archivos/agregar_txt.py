with open('Python\\archivos\\archivo3.txt', 'a', encoding='UTF-8') as file:
    # pasarle varias lineas a escriibir y no sobrescribe si se usan varias
    for i in range(5):
        file.write(f'Hola chamo {i+ 1}\n')
    
    # print()