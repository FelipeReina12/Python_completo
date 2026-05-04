# El ciclo for es una estructura de contról que nos permite repetir un bloque de código un número 
# determinado de veces. Es especialmente útil cuando queremos iterar sobre una secuencia de elementos, como 
# una lista, una tupla, un diccionario o un rango de números.

# Iternado sobre una lista
animales = ["perro", "gato", "conejo", "hamster"]
# Iniciamos el ciclo for 
# donde "animal" es la variable que tomará el valor de cada elemento de la lista
for animal in animales: 
    print(animal)  # Imprime el valor actual de "animal" en cada iteración

# Iternado sobre un rango de números y multiplicando cada número por 2
numeros = [45, 98, 102, 56]
for numero in numeros:
    numero = numero * 2
    print(numero)  # Imprime el número multiplicado por 2 en cada iteración

# Iterando dos listas al mismo tiempo usando la función zip()
# Para usar la función zip() las listas deben tener la misma cantidad de elementos
for animal, numero in zip(animales, numeros):
    print(f"El animal es: {animal} y el número es: {numero}")

########## 3:40:34 ########## 


