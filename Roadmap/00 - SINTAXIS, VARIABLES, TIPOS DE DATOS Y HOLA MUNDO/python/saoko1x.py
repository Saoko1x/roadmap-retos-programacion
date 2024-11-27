# https://www.python.org/

# 1. Comentarios
#  - Los comentarios en Python comienzan con el signo # y se extienden hasta el final de la línea.
#  - Los comentarios multilinea se pueden realizar con comillas simples o dobles. 
# esto es un comentario en una línea 

''' 
Con tres comillas simples
podemos realizar comentarios
en varias lineas
'''

"""
Tambien lo podemos realizar
con comillas dobles
"""

# 2. Variables
#  - Las variables en Python se definen con el signo =.
#  - Las variables no necesitan ser declaradas con ningún tipo en particular y pueden incluso cambiar de tipo después de haber sido creadas.
#  - Las variables son case-sensitive.
#  - Las variables en Python no pueden comenzar con un número.
#  - Las variables en Python no pueden contener espacios.
#  - Las variables en Python no pueden contener caracteres especiales, excepto el guion bajo (_).
#  - Las variables en Python no pueden ser palabras reservadas.

# Variable
name = "Python"

# Constante
GRAVITY  = 9.81 

# 3. Tipos de Datos
#  - Los tipos de datos primitivos en Python son: str, int, float, bool, list, tuple, set, dict.
#  - Para conocer el tipo de dato de una variable se puede utilizar la función type().

# String
name = "Python"
print(type(name))

# Integer
age = 30
print(type(age))

# Float
height = 1.75
print(type(height))

# Boolean
is_python = True
print(type(is_python))

# 4. Hola Mundo
#  - Para imprimir un mensaje en la consola se utiliza la función print().
#  - Se pueden concatenar variables con texto utilizando la coma (,).
#  - Se pueden concatenar variables con texto utilizando el signo +.
#  - Se pueden concatenar variables con texto utilizando el método format().

print("¡Hola, " + name + "!")
