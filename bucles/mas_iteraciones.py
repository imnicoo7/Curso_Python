
frutas = ['banana', 'manzana','pera', 'guanabana', 'fresa', 'guayaba','limon']

#evitando que se coma una manzana con la setencia continue
for fruta in frutas:
    if fruta == 'guanabana':
        print(f'che, la {frutas[3]} no nos vamos a comer')
        continue
    print(f'me voy a comer una {fruta}')
    
#evitando que el bucle siga ejecutandose (break) y si ponemos else, no se ejecutara
for fruta in frutas:
    print(f'che me estoy comiendo {fruta}')
    if fruta == frutas[4]:
        print(f'che, la {frutas[4]} me cayo de putas, no comere más')
        print('no como mas')
        break
else:
    print('terminado')
    
#recorrer una cadena de texto
hola = 'hola viejo mamado'

for letra in hola:
    print(letra)
    
#for en una sola linea de codigo (elevamos los numeros)
numeros = [3,5,2,3,6]

numeros_duplicados = [x**3 for x in numeros]
print(numeros_duplicados)

