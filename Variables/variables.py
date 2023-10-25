# las variables se declaran y despues se definen, y se pueden modificar
a = 1
a = 8
b = 4
c = a + b
print(c)

nombre = 'Nico' 

#definir variables con snake_case
nombre_completo = f'{nombre} Gutierrez'

#concatenar con f strings
bienvenida = f'Hola {nombre_completo} ¿cómo estás? :D'

del nombre #borrar una variable
print(bienvenida)

#Operadores de pertenencia (in, not in )
print('ola' in bienvenida)#con el in buscara si se encuentra en esa variable la palabra anterior 

print('ola' not in bienvenida)#con el not in buscara si no se encuentra en esa variable la palabra anterior


#case sensitive