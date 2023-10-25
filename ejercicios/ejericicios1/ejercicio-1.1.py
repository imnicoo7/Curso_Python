#promedios de duración
otros_cursos_min = 2.5 
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

#duración de crudo
crudo_promedio = 5
crudo_dalto = 3.5


#Diferencias de duración

diferencia_con_min = 100 - dalto_curso/ otros_cursos_min* 100
diferencia_con_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_con_promedio = 100 - dalto_curso/ otros_cursos_promedio * 100

#calculado el porcentaje de tiempo vacío removido
tiempo_vacio_promedio = 100 - otros_cursos_promedio *1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso* 1000 // crudo_dalto / 10

#mostrando las diferencias de duración (ejercicio A)
print('El curso de Dalto dura:')
print('------------------')
print(f'Un {diferencia_con_min}% menos que el más rápido')
print(f'Un {diferencia_con_max}% menos que el más lento')
print(f'Un {diferencia_con_promedio}% menos que el promedio')
print('------------------')

#Mostrandola cantidad de espacios vacios que se remueven (ejercicio B)
print(f'Un curso promedio elimina un {tiempo_vacio_promedio}% de tiempo vacio')
print(f'Este curso elimina un {tiempo_vacio_dalto}% de teiempo vacio')
print('------------------')

#mostrando diferencias si los cursos durararan 10 horas
print(f'Ver 10 horas de este curso equivale a ver: {otros_cursos_promedio * 100 //dalto_curso / 10} horas de otros cursos')

print(f'Ver 10 horas de otros cursos equivale a ver: {dalto_curso * 100 // otros_cursos_promedio / 10} horas de este curso')

print('------------------')
