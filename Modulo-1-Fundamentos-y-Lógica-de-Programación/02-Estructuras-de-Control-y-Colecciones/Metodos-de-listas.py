# Crear una lista con list()
lista = list(["Felipe", "Clarinete", 36,  "Mackbook", "Nintendo"])

# Devolver la cantidad de elementos de una lista
cantidad_elementos = len(lista)

print(cantidad_elementos)

# Agregar un elemento al final de la lista
lista.append("Guitarra")  # El método append() no devuelve nada

# Agregar un elemento a la lista en una posición específica
lista.insert(2, "Piano")

# Agregar varios elementos a la lista
lista.extend(["Bajo", "Bateria"])  # Es como agregar una lista a una lista al final de la misma

# Eliminar un elemento de la lista por su índice
lista.pop(3) 

# Eliminar el último elemento de la lista
lista.pop(-1)

# Remover un elemento de la lista por su valor
lista.remove("Nintendo")  # Si hay varios elementos con el mismo valor, solo se eliminará el primero que se encuentre

# Eliminar todos los elementos de la lista
# lista.clear()  # La lista queda vacía, pero sigue existiendo

# Ordenar los elementos de la lista de forma ascendente
lista.sort()  # sort no permite ordenar elementos de diferentes tipos
# Ordenar los elementos de la lista de forma descendente
lista.sort(reverse=True)

# Invierte los elementos de la lista
lista.reverse()

# Verificar la posción de un elemento en la lista, si es que existe
posicion = lista.index("Piano")  # Si el elemento no existe, se genera un error
print(posicion)

print(lista)  # Aquí se imprime es la lista con el nuevo elemento agregado

# print(dir(lista)) # Aquí se muestra una lista de todos los métodos disponibles para las listas en Python






