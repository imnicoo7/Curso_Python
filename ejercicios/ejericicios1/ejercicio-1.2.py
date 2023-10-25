#le pedimos al usuario que nos diga una frase (o varias)
frase = input('decime una frase y te calculo cuanto tardarías si tuvieras que decirlas: ')

#creamos una lista con todas las palabras de la frase (se separan cada vez que haya un espacio en blanco)
palabras_separadas = frase.split()
print(palabras_separadas)

#usamos len() para ver la cantidad de elementos que hay en una lista
cantidad_de_palabras = len(palabras_separadas)

#en caso de que tarde más de un minuto en decirlo, le decimos que pare un poco
if cantidad_de_palabras >= 120:
    print('che maestro, no te pedi un testamento')

#calculamos cuanto tardaria decir las palabras y se la decimos
print(f'Maestro dijiste {cantidad_de_palabras} palabras, y tardarías {cantidad_de_palabras/2} segundos en decirlo')
print(f'Dalto lo diría en {round(cantidad_de_palabras/2/1.3 ,2)} segundos')
