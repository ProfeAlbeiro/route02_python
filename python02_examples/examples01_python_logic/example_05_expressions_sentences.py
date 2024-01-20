# Variables
print('\n' + ('-' * 230))
print("Variables\n")
_user_code = 'user_01'
user_name = 'Albeiro'
user_lastname = 'Ramos V.'
user_age = 40
user_height = 1.72
user_blood_gr = 'O'
user_blood_tp = '+'
user_is_activate = True
print("     _user_code = 'user_01'")
print("     user_name = 'Albeiro'")
print("     user_lastname = 'Ramos'")
print("     user_age = 40")
print("     user_height = 1.72")
print("     user_blood_gr = 'O'")
print("     user_blood_tp = '+'")
print("     user_is_activate = True")

# Concatenar    : print( , )
print('\n' + ('-' * 230))
print("Concatenar    : print( , )\n")
print("print('Mi código de usuario es', _user_code,'. Soy', user_name, user_lastname, ', tengo', user_age, 'años , mi altura es de', user_height, 'mts , mi tipo de sangre es', user_blood_gr, user_blood_tp, ', aparezco activo en el sistema, es decir, como', user_is_activate)")
print('\n     Mi código de usuario es', _user_code,'. Soy', user_name, user_lastname, ', tengo', user_age, 'años , mi altura es de', user_height, 'mts , mi tipo de sangre es', user_blood_gr, user_blood_tp, ', aparezco activo en el sistema, es decir, como', user_is_activate)

# Concatenar    : print( + )
print('\n' + ('-' * 230))
print("Concatenar    : print( + )\n")
print("print('Mi código de usuario es ' + _user_code + '. Soy ' + user_name + ' ' + user_lastname + ', tengo ' + str(user_age) + ' años, mi altura es de ' + str(user_height) + ' mts, mi tipo de sangre es ' + user_blood_gr + user_blood_tp + ', aparezco activo en el sistema, es decir, como ' + str(user_is_activate)")
print('\n     Mi código de usuario es ' + _user_code + '. Soy ' + user_name + ' ' + user_lastname + ', tengo ' + str(user_age) + ' años, mi altura es de ' + str(user_height) + ' mts, mi tipo de sangre es ' + user_blood_gr + user_blood_tp + ', aparezco activo en el sistema, es decir, como ' + str(user_is_activate))

# Concatenar    : +
print('\n' + ('-' * 230))
print("Concatenar    : +\n")
template = 'Mi código de usuario es ' + _user_code + '. Soy ' + user_name + ' ' + user_lastname + ', tengo ' + str(user_age) + ' años, mi altura es de ' + str(
    user_height) + ' mts, mi tipo de sangre es ' + user_blood_gr + user_blood_tp
print("     template = 'Mi código de usuario es ' + _user_code + '. Soy ' + user_name + ' ' + user_lastname + ', tengo ' + str(user_age) + ' años, mi altura es de ' + str(user_height) + ' mts, mi tipo de sangre es ' + user_blood_gr + user_blood_tp")
print("     print(template) =", template)

# Concatenar    : f {}
print('\n' + ('-' * 230))
print("Concatenar strings : f {}\n")
template = f'Mi código de usuario es {_user_code}. Soy {user_name} {user_lastname}, tengo {user_age} años, mi altura es de {user_height} mts, mi tipo de sangre es {user_blood_gr}{user_blood_tp}'
print("     template = f'Mi código de usuario es {_user_code}. Soy {user_name} {user_lastname}, tengo {user_age} años, mi altura es de {user_height} mts, mi tipo de sangre es {user_blood_gr}{user_blood_tp}'")
print("     print(template) =", template)

# Concatenar    : format()
print('\n' + ('-' * 230))
print("Concatenar strings : format()\n")
template = 'Mi código de usuario es {}. Soy {} {}, tengo {} años, mi altura es de {} mts, mi tipo de sangre es {}{}'.format(_user_code, user_name, user_lastname, user_age, user_height, user_blood_gr, user_blood_tp)
print("     template = 'Mi código de usuario es {}. Soy {} {}, tengo {} años, mi altura es de {} mts, mi tipo de sangre es {}{}'.format(_user_code, user_name, user_lastname, user_age, user_height, user_blood_gr, user_blood_tp)")
print("     print(template) =", template)

# Crear una tabla de datos
print('\n' + ('-' * 230))
print("Crear una tabla de datos\n")
print('+' + ('-' * 79) + '+')
print('| Code\t\t| Nombre\t| Apellido\t| Edad\t| Estat\t| Sang\t| Est\t|')
print('+' + ('-' * 79) + '+')
print('| {}\t| {}\t| {}\t| {}\t| {}\t| {} {}\t| {}\t|'.format(_user_code, user_name, user_lastname, user_age, user_height, user_blood_gr, user_blood_tp, user_is_activate))
print('+' + ('-' * 79) + '+\n')

print(('-' * 230) + '\n')