# Operadores aritméticos
print(2 + 2)
print(2 - 2)
print(2 * 2)
print(2 / 2)
print(2 % 2)
print(2 ** 2)
print(2 // 2)

# Operadores lógicos
print(True and True)
print(True or False)
print(not True)

# Operadores de comparación
print(2 == 2)
print(2 != 2)
print(2 > 2)
print(2 < 2)
print(2 >= 2)
print(2 <= 2)

# Operadores de asignación
a = 2
print(a)

# Operadores de identidad
print(2 is 2)
print(2 is not 2)

# Operadores de pertenencia
print(2 in [2, 3, 4])
print(2 not in [2, 3, 4])

# Operadores de bits
print(2 & 2)
print(2 | 2)
print(2 ^ 2)
print(~2)
print(2 << 2)
print(2 >> 2)

# Estructuras de control
if True:
    print("if")
elif True:
    print("elif")
else:
    print("else")

for i in range(10):
    print(i)

while True:
    print("while")
    break

try:
    raise Exception("Error")
except Exception as e:
    print(e)
finally:
    print("finally")

# DIFICULTAD EXTRA
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)
