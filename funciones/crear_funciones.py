#crear una función simple
def sumar ( ):
    print(3+2) 
sumar()

#crear una funcion con parametros
print('----------------')
def saludar (nombre, sexo):
    sexo = sexo.lower()
    if sexo == 'hombre':
        adjetivo = 'chamo'
    elif sexo == 'mujer':
        adjetivo = 'reina'
    else:
        adjetivo = 'amor'
        
    print(f'hola {nombre}, como estas {adjetivo}, todo bien o que?')
    
saludar('Nicolas', 'HombRE')
saludar('Sofia', 'mujER')
saludar('Pedro', 'no lo se')
