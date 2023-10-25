archivo = open('Python\\archivos\\archivo.txt', encoding='UTF-8')

# Leer el archivo
# leido =  archivo.read()

# Leer la primera linea
# one_line = archivo.readline()

# Leer linea por linea
lines = archivo.readlines()

# Cerrar el archvio
close = archivo.close()

print(lines)