# Descripción del Objetivo o Problema a resolver, organizado como Sistema [Entradas, Proceso y Salidas]
print('\n' + ('-' * 60))
print('Identificadores, constantes, variables y tipos de datos')
print(('-' * 60) + '\n')
	
# Declarar constantes, variables y/o dimensionar arreglos asignando valores.

# Constantes (En mayúscula sostenida, aunque en Python no aplica)
APP = 'CALCULADORA'

# Variables
name = 'Albeiro'
operation = 'Suma'
num_01 = 5
num_02 = 9.3
result = 14.3
return_to = True

# Variables privadas : Guión bajo ( _ )
_code = '1'

# Variables super privadas : Doble guión bajo ( __ )
__do_not_touch = 'something important'

# Entrada de Datos: Pueden ser solicitados o no
	
# Proceso: Determinar los requerimientos y validaciones. Generalmente,	
#          se usan las estructuras de control: Secuencial, condicional, repetición.
	
# Salida de Datos: Resultado(s). Pueden ser parte del proceso.

# Identificadores   :   type()
print('Identificadores          :   Reglas para nombrar')
print()
print("Hola");
print('\n' + ('-' * 60))

# Tipos de datos    :   type()
print('Tipos de datos           :   type()')
print()
print("     APP = 'CALCULADORA'","      ", type(APP))
print("     _code = '1'","              ", type(_code))
print("     name = 'Albeiro'","         ", type(name))
print("     operation = 'Suma'","       ", type(operation))
num_01 = 5
num_02 = 9.3
result = 14.3
return_to = True

# PROYECTO DE EJEMPLO: CALCULADORA
print('\n\n' + ('*' * 60) + '\n')
print(('*' * 19) + ' PROYECTO DE EJEMPLO ' + ('*' * 20))
print('\n' + ('*' * 60) + '\n')
print(APP)
print()
print("     code            :", _code)
print("     name            :", name)
print("     operation       :", operation)
print("     first_number    :", num_01)
print("     second_number   :", num_02)
print("     result          :", result)
print("     return_to       :", return_to)
print('\n' + ('*' * 60) + '\n')