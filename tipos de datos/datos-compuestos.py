#listas
lista = ['Nico', 'Gutierrez', True, 1.85]

#tupla
tupla = ('Nico', 'Gutierrez', True, 1.85)

#la tupla no se puede modificar, pero la lista sí
print(lista)
print(tupla)

#creando un conjunto (set), no se accede a elementos por indice, no almacena datos duplicados

conjunto = {'Nico', 'Gutierrez', True, 1.85}

#diccionario (dict) (la estructura es key:valor)
diccionario = {
    'nombre':'Nicolas',
    'edad': 22,
    'cumpleaños': '27/09',
    'estatura' : 1.69
}

print(diccionario['cumpleaños'])