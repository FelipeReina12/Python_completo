# Las tuplas son similares a las listas y comparten varias de sus funciones y métodos, pero la diferncia es que las tuplas son inmutables
# es decir que no se pueden modificar una vez creadas

# Creación de una tupla
objetos = ("silla", "mesa", "lámpara", "estante")
print(objetos)

objetos_2 = 1, 2, 3, 4  # No hay necesidad de usar paréntesis para crear una tupla, aunque es común hacerlo para mejorar la legibilidad
print(type(objetos_2))

# Acceder a un elemento especifico de la tupla
print(objetos[0])  # Acceso a elementos de la tupla mediante índices

# Manejo de error
try:
    print(objetos.append("espejo")) # Esto generará un error porque las tuplas no tienen el método append() ya que son inmutables
except AttributeError as e:
    print(f"Error: {e}")

for i in objetos:
    print(i)