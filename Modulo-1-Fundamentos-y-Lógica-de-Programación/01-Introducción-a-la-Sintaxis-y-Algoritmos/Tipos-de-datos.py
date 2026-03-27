# Strings o cadenas de texto
# Las cadenas de texto se representan con comillas simples o dobles.
nombre = "Juan Felipe"
apellido = "Reina"

# Con comillas simples
cuidad = 'Bogotá'
departamento = 'Cundinamarca'

# Números enteros 
# Pueden ser positivos o negativos, pero no pueden tener decimales.
edad = 23
año_nacimiento = 2002
temperatura = -5
altura = -1.71

#Números decimales o flotantes
# Pueden ser positivos o negativos 
peso = 65.8
promedio_academico = 4.1
altitud = -5015.3
altura_negativa = -2.75

# Números complejos
# Se representan con la letra "j" o "J" al final del número
numero_complejo = 2 + 3j
otro_numero_complejo = 1 - 4j
# Estos números se utilizan principalmente en matemáticas y física para representar cantidades que tienen una parte real y una parte imaginaria

# Booleanos o lógicos
# Solo pueden tener dos valores: True (verdadero) o False (falso)
# Además, La primera letra tiene que ser mayúscula
es_estudiante = True
tiene_mascota = False
es_mayor_de_edad = True
es_colombiano = False

# Manipulación de cadenas de texto
# Operaciones comunes con cadenas de texto

# Concatenación: unir dos o más cadenas de texto
nombre = "Juan Felipe"
apellido = "Reina"
nombre_completo = nombre + " " + apellido
print(nombre_completo)

# Multiplicación: repetir una cadena de texto un número determinado de veces
string = "IA "
repetir = string * 3
print(repetir)

# Manipulación avanzada de cadenas de texto
# 1. Métodos de formateo (Visual)

# Convertir todo el texto a mayúsculas
texto = "Python es el mejor lenguaje de programación para aprender sobre intelignecia artificial"
texto_mayusculas = texto.upper()  
print(texto_mayusculas)
print(texto.upper())  # Importante no olvidar los paréntesis al llamar al método
# Se puede crear una variable para almacenar el resultado de la conversión o se puede imprimir directamente el resultado

# Convertir todo el texto a minúsculas
print(texto.lower())

# Convertir la primera letra de la frase a mayúscula
print(texto.capitalize())

# Convertir la primera letra de cada palabra a mayúscula
print(texto.title())

# Invierte mayúsculas por minúsculas y viceversa
print(texto.swapcase())

# 2. Métodos de Limpieza y Espaciado
# Elimina espacios en blanco (o caracteres específicos) al inicio y al final
texto_con_espacios = "  Python es     genial para      IA   "
print(texto_con_espacios.strip()) 

# Elimina espacios solo a la izquierda al inicio
print(texto_con_espacios.lstrip())

# Elimina espacios solo a la derecha al final
print(texto_con_espacios.rstrip())

# Centra el texto rodeándolo de un carácter (ej. para títulos en consola).
# Recive dos argumentos: el ancho total del texto centrado y el carácter que se usará para rellenar el espacio a los lados (opcional, por defecto es un espacio)
titulo = "Bienvenido a Python"
print(titulo.center(50, "*"))
print(titulo.center(50))  # Si no se especifica el carácter, se usará un espacio por defecto

# Reemplaza todas las ocurrencias de un texto por otro texto
# Se pueden encadenar varios reemplazos en una sola línea
texto_con_errores = "Pythn es un lenaje de programsion muy pdpular"
print(texto_con_errores.replace("Pythn", "Python").replace("lenaje", "lenguaje").replace("programsion", "programación").replace("pdpular", "popular"))

# 3. Métodos de Búsqueda y Validación
# Devuelve el índice (posición) de la primera aparición. Si no existe, devuelve -1.
texto_1 = "Python es un lenguaje de programación muy popular"
print(texto_1.find("lenguaje"))  # Duvuelve 13 porque la palabra "lenguaje" comienza en el índice 13
print(texto_1.find("Java"))  # Devuelve -1 porque la palabra "Java" no se encuentra en el texto

# Igual que find, pero si no existe, da un error (detiene el programa).
# print(texto_1.index("HTML"))  # Da un error porque la palabra "HTML" no se encuentra en el texto

# Cuenta cuántas veces aparece una letra o palabra.
texto_2 = "Python es un lenguaje de programación muy popular. Python es fácil de aprender."
print(texto_2.count("Python"))  # Devuelve 2 porque la palabra "Python" aparece dos veces en el texto

# Cuenta cuantas letras hay en el texto
cadena = "Pyton"
# En este caso el método len() se pasa como una función, ya que no es un método específico sino una función global
print(len(cadena)) # Devuelve 5 porque la palabra "Python" tiene 5 caracteres (letras)

# Devuelve True o False si el texto empieza con algo (útil para validar extensiones de archivos como .jpg o .pdf)
documento = "informe final.pdf"
print(documento.startswith("informe"))
print(documento.startswith("final"))

# Devuelve True o False si el texto termiona con algo (útil para validar extensiones de archivos como .jpg o .pdf)
archivo = "foto_vacaciones.jpg"
print(archivo.endswith(".jpg"))

# 4. Métodos de Separación y Unión (Los más potentes para IA)
# Rompe el string en una lista usando un separador (por defecto es el espacio).
frase = "Python es el mejor lenguaje de programación para aprender sobre inteligencia artificial"
print(frase.split())  # Devuelve una lista de palabras separadas por espacios

# Une los elementos de una lista en un solo string usando el texto original como "pegamento"
# Primer se le pasa el texto que se usará como separador entre los elementos de la lista, y luego se llama al método join() y se pasa como argumento la lista que se desea unir
palabras = ["Python", "es", "el", "mejor", "lenguaje", "de", "programación"]
print(" ".join(palabras))

# Rellena con ceros a la izquierda (muy usado en nombres de archivos o códigos ID).
# Se pasa como argumento la longitud total que se desea que tenga el string resultante, incluyendo los ceros
numero = "90118"
print(numero.zfill(10))  # Convierte el número a string y luego rellena con ceros a la izquierda hasta que tenga una longitud total de 10 caracteres en total, incluyendo los ceros

# Para poder ver que métodos se pueden usar con un tipo de dato específico, se puede usar la función dir() y pasar como argumento el tipo de dato o una variable de ese tipo de dato
print(dir(frase))