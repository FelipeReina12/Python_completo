# Entrada de Datos 
# Para solicitar datos al usuario, se utiliza la función input()
nombre_usuario = input("Por favor ingresa tu nombre: ")
# Esto quedará almacenadio en la variable nombre_usuario, y se puede usar posteriormente en el programa
print("Hola, " + nombre_usuario.title() + "! Bienvenido a Python.")

# Por defecto todo lo que entra por un input() es un string pero podemos convertirlo a otros tipos de datos como int o float usando las funciones de conversión correspondientes
# Solicitar un número entero al usuario
# Primero convertimos el resultado del input a un entero usando la función int()
edad_usuario = int(input("Ingresa tu edad: "))
print(f"Tu edad es: {edad_usuario} años.")

# Solicitar un número decimal al usuario
# Se convierte el resultado del input a un número decimal usando la función float()
altura_usuario = float(input("Ingresa tu altura en metros: "))
print(f"Tu altura es: {altura_usuario} metros.")

# Combinando todo 

print(f"Hola, {nombre_usuario.title()}, Tienes {edad_usuario} años y mides {altura_usuario} metros. !Bienvenido a Python¡.")

#Operadores matemáticos
# Suma
a = int(input("Ingresa un número entero: "))
b = int(input("Ingresa otro número entero: "))
suma = a + b
print(f"La suma de {a} + {b} es: {suma}")

# Resta
resta = a - b
print(f"La resta de {a} - {b} es: {resta}")     

# Multiplicación
multiplicacion = a * b
print(f"La multiplicación de {a} * {b} es: {multiplicacion}")

# División
division = a / b
print(f"La división de {a} / {b} es: {division}")   

# Módulo (resto de la división)
# Es muy util para saber si un número es par o impar, tambien para obtener el último dígito de un número
modulo = a % b
print(f"El módulo de {a} % {b} es: {modulo}")

# Exponenciación
# Eleva un número a la potencia de otro número
exp = a ** b
print(f"{a} elevado a la potencia de {b} es: {exp}")

# Se utilizan para comparar dos valores y obtener un resultado booleano (True o False)
# Igualdad (==)
igual_que = 5 == 5
print(f"¿5 es igual a 5? {igual_que}")

# Desigualdad (!=) 
diferente_que = 5 != 3
print(f"¿5 es diferente a 3? {diferente_que}")

# Mayor que (>)
mayor_que = 10 > 7
print(f"¿10 es mayor que 7? {mayor_que}")

# Menor que (<)
menor_que = 4 < 6
print(f"¿4 es menor que 6? {menor_que}")

# Mayor o igual que (>=)
mayor_o_igual_que = 8 >= 8
print(f"¿8 es mayor o igual que 8? {mayor_o_igual_que}")

# Menor o igual que (<=)
menor_o_igual_que = 3 <= 5
print(f"¿3 es menor o igual que 5? {menor_o_igual_que}")
