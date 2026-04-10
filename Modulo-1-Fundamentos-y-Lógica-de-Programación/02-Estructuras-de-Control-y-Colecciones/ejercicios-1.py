# Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7 
otros_cursos_promedio = 4
dalto_curso = 1.5

# Duracipon de crudos
crudo_promedio = 5
crudo_dalto = 3.5

# Diferencias de duración
print("El curso de dalto dura: ")
diferencia_con_min = 100 - dalto_curso / otros_cursos_min * 100
print(f'- {round(diferencia_con_min, 2)}% menos que el curso más corto')

diferencia_con_max = 100 - dalto_curso / otros_cursos_max * 100
print(f'- {round(diferencia_con_max, 1)}% menos que el curso más largo')

diferencia_con_promedio = 100 - dalto_curso / otros_cursos_promedio * 100
print(f'- {round(diferencia_con_promedio, 2)}% menos que el promedio de duración de los otros cursos')

print("--------------------------------------------------------------------------------------------------------------")

# Calculando el porcentaje de tiempo vacío
tiempo_vacio = 100 - otros_cursos_promedio / crudo_promedio * 100
print(f'Un curso promedio elimina un {round(tiempo_vacio, 2)}% de tiempo vacío')
tiempo_vacio_dalto = 100 - dalto_curso / crudo_dalto * 100
print(f'Este curso eliminó el {round(tiempo_vacio_dalto, 2)}% de tiempo vacío') 

print("--------------------------------------------------------------------------------------------------------------")

# Mostrand diferencias si los cursos duraran 10 horas
print(f'ver 10 horas de este curso equivale a ver {round(otros_cursos_promedio / dalto_curso * 10, 2)} horas de otros cursos')
print(f'ver 10 horas de otros cursos equivale a ver {round(dalto_curso / otros_cursos_promedio * 10, 2)} horas de este curso')