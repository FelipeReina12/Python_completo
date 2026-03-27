# Los condicionales son estructuras de control que permiten ejecutar diferentes bloques de código según ciertas condiciones. 
# En Python, los condicionales se implementan utilizando las palabras clave `if`, `elif` y `else`.
# La estructura de los condicionales es la siguiente: 
# if condición:
#     bloque de código a ejecutar si la condición es verdadera
# if
edad = 17 
if edad >= 18:
    print("Puedes votar.")  # No imprime nada porque la condición es falsa

edad_2 = 23
if edad_2 >= 18:
    print("Puedes votar.")  # Imprime "Puedes votar." porque la condición es verdadera

# if-else
#El bloque else debe estar fuera del bloque if
inscripcion = True
if inscripcion == True:
    print("Inscripción exitosa.") 
else:
    print("Error en la inscripción.") 

# else-if o elif
# Se utiliza para evaluar múltiples condiciones de manera secuencial.
# Elif tambien va fuera del bloque if
plata = 1200000
if plata >= 1000000:
    print("Estás bien económicamente.")
elif plata >= 500000:
    print("Tienes una situación económica aceptable.")
elif plata >= 100000:
    print("Tu situación económica es precaria.")
elif plata >= 0:
    print("Tu situación económica es muy precaria.")
else:
    print("Necesitas mejorar tu situación económica.")

# if anidados
# Se pueden anidar condicionales dentro de otros condicionales para evaluar condiciones más complejas.
ingreso_mensual = 800000
gastos_mensuales = 600000
if ingreso_mensual > gastos_mensuales:
    print("Manejas bien tus finanzas.")
    if ingreso_mensual - gastos_mensuales > 200000:
        print("Tienes un buen ahorro mensual.")
    else:
        print("Tu ahorro mensual es limitado.")