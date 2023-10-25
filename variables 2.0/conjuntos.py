# creando un conjunto con set()
conjunto = set(['dato1', ' dato2'])

#metiendo un conjunto dentro de otro conjunto
conjunto1 = frozenset(['melo', 'melo2'])
conjunto2 = {conjunto1, 'queso'}
print(conjunto2) 

#teoria de conjuntos
conjunto_a = {1,2,3,6}
conjunto_b = {1,2,6}

#verificando si b es subconjunto de a
resultado = conjunto_b.issubset(conjunto_a)
#otra forma
resultado = conjunto_b <= conjunto_a

#verificando si b es superconjunto de a
resultado = conjunto_b.issuperset(conjunto_a)
#otra forma
resultado = conjunto_b > conjunto_a

#verificar si hay un numero en común
resultado = conjunto_b.isdisjoint(conjunto_a)
print(resultado)