is_single = True
print(is_single)
print(type(is_single))
is_single = False
print(is_single)
print(type(is_single))
print(not True)
print(not False)
is_single = not is_single
print(is_single)

# and
print('AND')
print('True and True =>', True and True)
print('True and False =>', True and False)
print('False and True =>', False and True)
print('False and False =>', False and False)
print(10 > 5 and 5 < 10)
print(10 > 5 and 5 > 10)
stock = input('Ingrese el número de stock => ')
stock = int(stock)
print(stock >= 100 and stock <= 1000)
# or
print('OR')
print('True or True =>', True or True)
print('True or False =>', True or False)
print('False or True =>', False or True)
print('False or False =>', False or False)
role = input('Digita el rol => ')
print(role == 'admin' or role == 'seller')

print(not True)
print(not False)
# not and
print('AND')
print('not(True and True) =>', not (True and True))
print('not(True and False) =>', not (True and False))
print('not(False and True) =>', not (False and True))
print('not(False and False) =>', not (False and False))
stock = input('Ingrese el número de stock => ')
stock = int(stock)
print(not (stock >= 100 and stock <= 1000))

# Operadores lógicos
print("Operadores lógicos")
print()
print("     x = 2")
print("     y = 3")
print("     a = 5")
print("     b = 7")
print()
# AND
print("AND: Es verdadero cuando todos los valores son verdaderos")
print("     print((x < y) and (a < b)) =", (x < y) and (a < b))
print("     print((x < y) and (a > b)) =", (x < y) and (a > b))
print()
# OR
print(" OR: Es verdadero cuando algún valor es verdadero")
print("     print((x < y) or (a < b)) =", (x < y) or (a < b))
print("     print((x > y) or (a > b)) =", (x > y) or (a > b))
print()
# NOT
print("NOT: Cambia el resultado de falso a verdadero o de verdadero a falso")
print()
# Condicional if-else
print("Condicional if-else")
print()
print("     message = '' ")
print()
print("     if x < y:")
print("         message = 'x es menor que y'")
print("     else:")
print("         message = 'x no es menor que y'")
message = ''
if x < y:
    message = 'x es menor que y'
else:
    message = 'x no es menor que y'
print()
print("     print(message) = ", message)

print()
