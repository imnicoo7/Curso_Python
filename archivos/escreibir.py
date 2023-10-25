with open('Python\\archivos\\archivo2.txt', 'w', encoding='UTF-8') as file:
    # se sobrescribe el archivo
    # file.write('vete a comer')
    
    # pasarle varias lineas a escriibir y no sobrescribe si se usan varias
    file.writelines(['hola crack\n', 'hola crack\n' 'hola crack\n'])
    file.writelines(['hola crack\n', 'hola crack\n' 'hola crack\n'])
    
    # print()