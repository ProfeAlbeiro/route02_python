# Variables dinámicas
print('-' * 50)
print('Variables dinámicas')
print()
variable = 'user_01'
print("     variable = 'user_01'")
print("     type(variable) =", type(variable))
print()
variable = 'Albeiro'
print("     variable = 'Albeiro'")
print("     type(variable) =", type(variable))
print()
variable = 'Ramos'
print("     variable = 'Ramos'")
print("     type(variable) =", type(variable))
print()
variable = 40
print("     variable = 40")
print("     type(variable) =", type(variable))
print()
variable = 1.72
print("     variable = 1.72")
print("     type(variable) =", type(variable))
print()
variable = 'O'
print("     variable = 'O'")
print("     type(variable) =", type(variable))
print()
variable = '+'
print("     variable = '+'")
print("     type(variable) =", type(variable))
print()
variable = True
print("     variable = False")
print("     type(variable) =", type(variable))
print()

# Convertir a cadena: str()
print('-' * 50)
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
print()

print('-' * 50)
print()