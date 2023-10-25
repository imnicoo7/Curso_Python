animales = ['Perro', 'Gato','Loro', 'Cocodrilo', 'Pez']

#recorriendo lista animales
for animal in animales:
    print(animal)

numeros = [10,12,12,70,12]

#recorriendo lista numeros y multiplicar 2
for numero in numeros:
    resultado = numero * 2
    print(resultado)
    
#iterando 2 listas del mismo tamaño al mismo tiempo
for animal, numero in zip(animales, numeros):
    print(f'Valor lista animales: {animal}')
    print(f'Valor lista numeros: {numero * 2}')

#recorriendo pasandole un rango    
for num in range(5,10):
    print(num)
    
#forma no optima de recorer una lista con su indice (no funciona en conjuntos)
for num in range(len(numeros)):
    print(f'no hacerlo asi {numeros[num]}')
    
# forma correcta de recorrer una lista con su indice
for i, num in enumerate(numeros):
    
    print(f'el índice es {i} y el valor es {num}')
    
#usando el for/else
for numero in numeros:
    print(f'ejecutando el ultimo bucle, valor actual: {numero}')
else:
    print('el bucle termino')
    
#todo lo anterior funciona igualmente para tuplass y conjuntos
