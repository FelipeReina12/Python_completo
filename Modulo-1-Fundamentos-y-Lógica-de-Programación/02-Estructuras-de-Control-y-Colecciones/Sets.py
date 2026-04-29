# los sets son colecciónes desordenadas de elementos unicos, es decir que no se permiten elementos duplicados
# Son mutables, por lo que se pueden añadir y eliminar elementos
# Se definenen con {} o con ()
# Son útiles para eliminar elementos duplicados de una lista, realizar operaciones de conjuntos y verificar la pertenencia de un elemento a un conjunto 

frutas = {"apple", "orange", "banana", "coconut"}
print(len(frutas))  # Se imprime de manera aleatoria, no se garantiza el orden de los elementos

numeros = { 9, 8, 7, 6, 5, 4, 3, 2, 1 }
print(numeros)  # Los números si se imprimen en orden

a = set("abaracadabra")
print(a)  # Se imprimen los caracteres unicos de la palabra "abaracadabra"

# Tipo 1: Sets mutables, se pueden agregar nuevos elementos
b = set("cokie")  # Un set donde cada letra es un elemento 
b.add("yoguie")  # Se agrega un nuevo elemento al set
print(b)

# Tipo 2: Sets inmutables, frozenset, no se pueden agregar nuevos elementos
b = frozenset("python")
# Manejo de errores para evitar que el programa se detenga
try:  # Aquí se intenta apgregar un nuevo elemento al frozenset, lo cual genera un error
    b.add('k')  
except AttributeError as e:  # Se captura el error de tipo AttributeError, que es el que se genera al intentar agragar un nuevo elemento
    print(e)  # Se imprime el error que se genera al intentar agregar un nuevo elemento a un frozenset
print(b)

# Intersección de sets
# mi_set = {1, 2, 3, 4, 5}.intersection({3, 4, 5})  # Devuelve un nuevo set con los elementos que se encuentran en ambos sets
mi_set = {1, 2, 3, 4, 5} & ({3, 4, 5})  # Otra forma de hacerlo (siempre el otro set debe ir en paréntesis)
print(mi_set)

# Unión de sets
# otro_set = {10, 11, 12}.union({13, 14, 15})  # Devuelve un nuevo set con todos los elementos de ambos sets, sin duplicados
otro_set = {10, 11, 12, 13} | {13, 14, 15}  # Otra forma de hacerlo
print(otro_set)

# Elementos diferentes entre dos sets
# set_diferente = {1, 2, 3, 4, 5}.difference({1, 3, 6, 9})  # Devuelve un nuevo set con los elementos que se encuentran en el primer set pero no en el segundo
set_diferente = {1, 2, 3, 4, 5} - ({1, 3, 6, 9})  # Otra forma de hacerlo
print(set_diferente)

# Diferencia simétrica entre dos sets
dif_set = {1, 2, 3, 4, 5}.symmetric_difference({1, 3, 6, 9})  # Excluye a los elementos que se encuentran en ambos sets, devuelve un nuevo set con los elementos que se encuentran en el primer set pero no en el segundo y viceversa
print(dif_set)

# Verificar si un elemento se encuentra en un set
my_new_set = {1, 2, 3, 4, 5}.issuperset({1, 2})  # Devuelve True si el set contiene a todos los elementos del otro set, es decir, si el primer set es un superconjunto del segundo set
print(my_new_set)

# Verificar si un set es un subconjunto de otro set
my_new_set = {1, 2}.issubset({1, 2, 3, 4, 5})  # Devuelve True si el set se encuentra dentro de otro set, es decir, si el primer set es un subconjunto del segundo set
print(my_new_set)