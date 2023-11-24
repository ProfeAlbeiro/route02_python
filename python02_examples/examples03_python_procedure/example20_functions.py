# Definir una función
print()
print("*" * 27, "Definir una función", "*" * 28)
print()
print("     def funcion(parámetros):")
print("         return valor")

# Alcance de las variables: globales y locales
print()
print("*" * 15, "Alcance de las variables: globales y locales", "*" * 15)

# No se modifica la variable global
print("\nNo se modifica la variable global")
print()

num1 = 5 # variable global


def funcion():    
    num1 = 50  # variable local
    return num1


print("     num1 = 5 # variable global")
print()
print("     def funcion():")
print("         num1 = 50  # variable local")
print("         return num1")
print()
print("     print(funcion()) =", funcion())
print("     print(num1) =", num1)
print()

# Se modifica la variable global
print("-" * 76)
print("Se modifica la variable global")
print()


def funcion():
    global num1 # Usa la variable global
    num1 = 50  # Es la variable global
    return num1


print("     num1 = 5 # variable global")
print()
print("     def funcion():")
print("         global num1 # Usa la variable global")
print("         num1 = 50  # Es la variable global")
print("         return num1")
print()
print("     print(funcion()) =", funcion())
print("     print(num1) =", num1)

# Caso 01. Función SIN parámetros y SIN retorno de valor
print()
print("*" * 28, "Casos en Funciones", "*" * 28)
print("\nCaso 01. Función SIN parámetros y SIN retorno de valor")
print()

num1 = 5
num2 = 10


def funcion_caso_01():
    res = num1 + num2    
    print('     = La suma de', num1, 'más', num2, 'es', res)


print("     num1 = 5")
print("     num2 = 10")
print()
print("     def funcion_caso_01():")
print("         res = num1 + num2")
print("         print('La suma de', num1, 'más', num2, 'es', res)")
print()
print("     funcion_caso_01()")
funcion_caso_01()
print()
print("-" * 76)

# Caso 02. Función CON parámetros y SIN retorno de valor
print("Caso 02. Función CON parámetros y SIN retorno de valor")
print()


def funcion_caso_02(num1, num2):
    res = num1 + num2
    print('     = La suma de', num1, 'más', num2, 'es', res)


print("     def funcion_caso_02(num1, num2):")
print("         res = num1 + num2")
print("         print('La suma de', num1, 'más', num2, 'es', res)")
print()
print("     funcion_caso_02(5, 10)")
funcion_caso_02(5, 10)
print()
print("-" * 76)

# Caso 03. Función SIN parámetros y CON retorno de valor
print("Caso 03. Función SIN parámetros y CON retorno de valor")
print()

num1 = 5
num2 = 10


def funcion_caso_03():    
    res = num1 + num2
    return res


print("     num1 = 5")
print("     num2 = 10")
print()
print("     def funcion_caso_03():")
print("         res = num1 + num2")
print("         return res")
print()
print("     print('La suma de', num1, 'más', num2, 'es', funcion_caso_03())")
print('     = La suma de', num1, 'más', num2, 'es', funcion_caso_03())
print()
print("-" * 76)

# Caso 04. Función CON parámetros y CON retorno de valor
print("Caso 04. Función CON parámetros y CON retorno de valor")
print()


def funcion_caso_04(num1,num2):
    res = num1 + num2
    return res


print("     def funcion_caso_04(num1, num2):")
print("         res = num1 + num2")
print("         return res")
print()
print("     print('La suma de', num1, 'más', num2, 'es', funcion_caso_04(5, 10))")
print('     = La suma de', num1, 'más', num2, 'es', funcion_caso_04(5, 10))
print()
print("-" * 76)
print()