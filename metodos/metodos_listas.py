#crear lista con list()
lista = list([1,2,3])
print(lista)

#len cuenta la cantidad de elementos en una lista
cantidad_elementos = len(lista)
print(cantidad_elementos)

#append, agregar elementos a la lista
lista.append('queso')

#insert agrega un elemento a la lista en un indice especifico
lista.insert(1, 'jamón')

#extend, agrega varios elementos a la lista, toca ponerle un []
lista.extend([10, 'pan', False, ' juan', 'pepe'])
lista.extend([10,  False, False, True])

#.pop  elimina elementos por su indice
lista.pop(3)
#para eliminar el ultimo: -1, el penultimo: -2 y así sucesivamente
lista.pop(-2)
#.remove, remueve elementos por su valor, decir el valor especifico
lista.remove(10)

#eliminar todos los elementos de la lista .clear
#lista.clear()

#ordena elementos de forma ascendentes, no funciona con cadenas de texto, solo numeros y booleanos

#lista.sort()
#lista.sort(reverse=True) #para ordenarlo a la inversa DE Forma ascendente

#.reverse invierte la lista, pero no igual que el anterior  
lista.reverse()

print(lista) 