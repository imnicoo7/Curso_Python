diccionario = {
    'nombre': 'Nicolas',
    'apellido': 'Gutierrez',
    'subs': 1.000
}

print(diccionario)

#keys() para mostrar los nombres de la claves 
claves = diccionario.keys()
print(claves)

#.get() obtener un elemento por su key, (si no encuentra el programa continua)
obtener_valor = diccionario.get('nombre')
print(obtener_valor)

#eliminar todos los elementos con .clear()
#diccionario.clear()

#eliminar elementos por su clave con .pop()
diccionario.pop( 'apellido')

#items() ibtener un elemento dict_items iterable
dict_iterable = diccionario.items()

print(dict_iterable)

