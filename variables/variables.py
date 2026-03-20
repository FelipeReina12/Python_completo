#Las variables se declaran y se definen
#También son modificables
a = 4
b = 5
c = True
d = a +b

nombre = "Juan"
nombre = "Cokie"
nombre = "Yoguie"
#Se está redifiniendo la variable. tendrá el valor de la ultima asignación
print(nombre)

numero = 22
numero += 1  #El valor que ya tiene mas lo que esté despues del igual
print(numero)

#Concatenación es la union de strings 
bienvenida = "Hola"
nombre = "Auron"
saludo = f"hola {nombre}  Como estás"  #f lo que hace es tomar un dato y convertirlo a texto
print(saludo)

#Borrar una variable
# del bienvenida
# print(bienvenida)

#Operadors de oertenencia (in, not in)
print("Juan" in nombre)  #Busca una palabra en una variable
print("Felipe" not in nombre)  #Busca si una palabra no está en una variable

#Definir una variable con camelCase (No recomendable para python)
nombreCompleto = "Felipe Reina"

#Definir una variable con snake_case (Recomendable para python)
nombre_completo_y_apellido = "Juan Felipe Reina"