# Descripción del Objetivo o Problema a resolver, organizado como Sistema [Entradas, Proceso y Salidas]
print('\n' + ('-' * 100))
print('Identificadores, constantes, variables y tipos de datos')
print(('-' * 100) + '\n')
	
# Declarar constantes, variables y/o dimensionar arreglos asignando valores.

# 1. Reglas del Idenfificador: Aplica para constantes, variables, arreglos,
#    listas, tuplas, diccionarios, funciones, clases, objetos, entre otros.

#     1.1. No se pueden utilizar palabras reservadas
#     1.2. Pueden contener números y letras
#     1.3. Deben ser semánticos
#     1.4. Iniciar en minúscula, salvo que sea una Clase
#     1.5. No deben comenzar con un número
#     1.6. Las constantes se declaran en mayúscula sostenida
#     1.7. No deben llevar comas, puntos, acentos, espacios en blanco o la letra 'ñ'
#     1.8. El guión bajo indica que es privada
#     1.9. Doble guión bajo es super privada. Su modificación implica daño general
#    1.10. Se sugiere que la longitud sea hasta de 8 caracteres

# 2. Constantes (En mayúscula sostenida, aunque en Python no aplica)
PI = 3.1416

# 3. Variables
name = 'Albeiro'
num_01 = 5
num_02 = 9.3
active = True

# 3.1. Variables privadas : Guión bajo ( _ )
_code = '001'

# 3.2. Variables super privadas : Doble guión bajo ( __ )
__do_not_touch = 'something important'

# Entrada de Datos: Pueden ser solicitados o no
	
# Proceso: Determinar los requerimientos y validaciones. Generalmente,	
#          se usan las estructuras de control: Secuencial, condicional, repetición.
	
# Salida de Datos: Resultado(s). Pueden ser parte del proceso.

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