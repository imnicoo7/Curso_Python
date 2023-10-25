cadena1 = 'Hola soy Nicolas'
cadena2 = 'Bienvenido Maquinola'
cadena3 = 'mango'
#metodos = datos . metodo ()

#convertir todo en mayuscula
mayusc = cadena1.upper()

#convertir todo en minuscula
minusc =  cadena2.lower()

#primera letra en mayuscula

fist_letra_mayusc = cadena2.capitalize()

#buscamos una cadena en otra cadena, si no hay coincidencias devuelve un -1
busqueda_find = cadena1.find('las')

#buscamos una cadena en otra cadena, si no hay coincidencias lanza una excepcion
busqueda_index = cadena1.index('N')

#Comprueba si la cadena es numerica, devolvera True si no False
es_Numeric = cadena3.isnumeric()

#si es alfanumérico devolvemos True, si no false
es_alfanumeric = cadena3.isalpha()

#contanmos coincidencias de una cadena, devuelve la cantidad de coincidencias
contar_coincidencia = cadena1.count('a')

#contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena2)

#verificamos si una cadena empieza con otra cadena dada, si es así devuelve true
empieza_con = cadena2.startswith('H')

#verificamos si una cadena termina con otra cadena dada, si es así devuelve true
termina_con = cadena2.endswith('a')

#remplaza un pedazo de la cadena dada por otra
cadena_nueva = cadena3.replace('mango', 'Fresa')

#separar cadenas con la cadena que lepasamos
separa_cadena = cadena1.split(' ')
print(separa_cadena)