#Datos que tienen a dentro otro dato

#Lista
lista = ["Felipe Reina", "Pyton", 1.71, True, 23, "Zetawise"]
print(lista)  #Imprime la lista
print(lista[1]) #Imprime el elemento en la posición asignada
print(len(lista))  #Imprime la cantidad de datos en la lista

#La diferncia entre las tuplas y las listas es que las tuplas no se pueden modificar

#Tuplas
tupla =("Juan", 23, "Nintendo", True, 1.71)
print(tupla)

lista[3] = "False"  #Se puede modificar
print(lista)

# tupla[2] = "Xbox"  #No se puede modificar
# print(tupla)