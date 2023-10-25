#creando un diccionario con dict
diccionario = dict(nombre = 'nico', apellido = 'castiyejo')

#las listas no pueden ser claves Y usamos frozenset para meter  conjuntos
diccionario = {('dalto', 'rancio'): 'jajjaaaaajajajajaajaaazs xzz<sxx<zq'}

#creando diccionarios con fromkeys() valor por defecto: none
diccionario = dict.fromkeys(['nombre', 'apellido'])

#creando diccionarios con fromkeys() cambiando el valor por defecto a 'nose'
diccionario = dict.fromkeys(['nombre', 'apellido'], 'Nose', 'sise')

print(diccionario)
