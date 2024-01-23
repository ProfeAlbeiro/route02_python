# Descripción del Objetivo o Problema a resolver, organizado como Sistema [Entradas, Proceso y Salidas]
print('\n' + ('-' * 100))
print('Conversiones')
print(('-' * 100) + '\n')
	
# Declarar constantes, variables y/o dimensionar arreglos asignando valores.
PI = 3.1416
name = 'Albeiro'
num_01 = 5
num_02 = 9.3
active = True
_code = '001'

# Entrada de Datos: Pueden ser solicitados o no
	
# Proceso: Determinar los requerimientos y validaciones. Generalmente,	
#          se usan las estructuras de control: Secuencial, condicional, repetición.

# Salida de Datos: Resultado(s). Pueden ser parte del proceso.

# Variables dinámicas
print('Variables dinámicas')
print()
variable = '3.1416'
print("     variable = 'CALCULADORA'", "    ", type(variable))
variable = '1'
print("     variable = '1'", "              ", type(variable))
variable = 'Albeiro'
print("     variable = 'Albeiro'", "        ", type(variable))
variable = 'Suma'
print("     variable = 'Suma'", "           ", type(variable))
variable = 5
print("     variable = 5", "                ", type(variable))
variable = 9.3
print("     variable = 9.3", "              ", type(variable))
variable = 14.3
print("     variable = 14.3", "             ", type(variable))
variable = True
print("     variable = True", "             ", type(variable))
print('\n' + ('-' * 100))

# Convertir a cadena: str()
print("Convertir a cadena: str()")
print()
user_age = 40
user_height = 1.72
user_is_activate = True
print("     user_age = 40")
print("     user_height = 1.72")
print("     user_is_activate = True")
print()
to_string = str(user_age)
print("     to_string = str(user_age)")
print("     print(to_string) =", to_string)
print("     print(type(to_string))", type(to_string))
print()
to_string = str(user_height)
print("     to_string = str(user_height)")
print("     print(to_string) =", to_string)
print("     print(type(to_string))", type(to_string))
print()
to_string = str(user_is_activate)
print("     to_string = str(user_is_activate)")
print("     print(to_string) =", to_string)
print("     print(type(to_string))", type(to_string))
print()

# De flotante a entero: int()
print('-' * 50)
print("De flotante a entero: int()")
print()
user_height = 1.72
to_int = int(user_height)
print("     user_height = 1.72")
print("     to_int = int(user_height)")
print("     print(to_int) =", to_int)
print("     type(to_int) =", type(to_int))
print()

# De entero a flotante: float()
print('-' * 50)
print("De entero a flotante: float()")
print()
user_age = 40
to_float = float(user_age)
print("     user_age = 40")
print("     to_float = float(user_age)")
print("     print(to_float) =", to_float)
print("     print(type(to_float)) =", type(to_float))
print()

# De cadena a entero: int()
print('-' * 50)
print("De cadena a entero: int()")
print()
user_age = '40'
print("     user_age = 40")
print("     print(type(user_age)) =", type(user_age))
to_int = int(user_age)
print("     to_int = int(user_age)")
print("     print(type(to_int)) =", type(to_int))
print()

# De cadena a flotante: float()
print('-' * 50)
print("De cadena a flotante: float()")
print()
user_height = '1.72'
print("     user_height = '1.72'")
print("     print(type(user_height)) =", type(user_height))
to_float = float(user_height)
print("     to_float = float(user_height)")
print("     print(type(to_float)) =", type(to_float))

# PROYECTO DE EJEMPLO: CALCULADORA
print('\n\n' + ('-' * 100) + '\n')
print(APP)
print()
print("     code            :", _code)
print("     name            :", name)
print("     operation       :", operation)
print("     first_number    :", num_01)
print("     second_number   :", num_02)
print("     result          :", result)
print("     return_to       :", return_to)
print('\n' + ('-' * 100) + '\n')


# ----------------------------------------------------------------------------------------------------------------------------

# Tipos de datos    :   type()
print('Tipos de datos    :   type()')
print()
print('     PI                  :   ', PI, '                 ', type(PI), '     Constante')
print('     _code               :   ', _code,'                    ', type(_code), '       Variable privada')
print('     __do_not_touch      :   ', __do_not_touch, '    ', type(__do_not_touch), '       Variable super privada')
print('     name                :   ', name, '                ', type(name), '       Variable Cadena')
print('     num_01              :   ', num_01, '                      ',  type(num_01), '       Variable Entera')
print('     num_02              :   ', num_02, '                    ', type(num_02), '     Variable Decimal')
print('     active              :   ', active, '                   ', type(active), '      Variable Booleana')
print('\n' + ('-' * 100))