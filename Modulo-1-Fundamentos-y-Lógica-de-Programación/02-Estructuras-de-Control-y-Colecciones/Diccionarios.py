# Definimos el diccionario
diccionario = {
    "nombre": "Felipe",
    "instrumento": "Clarinete",
    "edad": 23,
    "computador": "Acer",
}
# Extraer las claves del diccionario y almacenarlas en una variable
claves = diccionario.keys() # devuelve una lista con las claves del diccionario. tambien sirve para iterar
print(claves)

# Extraer los un valor específico del diccionario y almacenarlos en una variable
valores = diccionario.get("nombre") # devuelve el valor asociado a la clave "nombre"
print(valores)
# get() se usa para evitar errores al intentar acceder a una clave que no existe en el diccionario, ya que devuelve None

# Podemos llamar alguna clave o valor como si fuera una lista pero no es recomendable
dic_num = {
    1: "uno", 
    2: "dos",
    3: "tres",
    4: "cuatro",
}
print(dic_num[2]) # Devuelve el valor asociado a la clave 2

# Eliminar todos los elementos de la lista
# diccionario.clear()
# print(diccionario)

# Eliminando un elemento del diccionario
diccionario.pop("computador") # Elimina la clave "computador" y su valor asociado
print(diccionario)

# Obteniendo un elemento dic_items ierable
diccionario_items = diccionario.items() # Devuelve una lista de tuplas con las claves y valores del diccionario
print(diccionario_items)