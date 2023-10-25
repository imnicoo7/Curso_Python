diccionario = {
    'nombre': 'Nico',
    'apellido': 'Apellido',
    'subs': 10000
}
# recorriendo el diccionario para obtener las claves y los valores
for key in diccionario:
    print(f'el valor de la clave es: {key} ')

print('-------------------------------')
# recorriendo el diccionario para obtener las claves y los valores
for datos in diccionario.items():
    key = datos[0]
    dato = datos[1]
    print(f'el valor de la clave es: {key} y el valor es: {dato}')
   
    