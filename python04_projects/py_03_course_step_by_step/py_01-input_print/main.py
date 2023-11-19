# Inicio de la aplicación
if __name__ == '__main__':
      # Crear Usuario
      print('\n' + ('-' * 82))
      print("Crear Usuario\n")
      _user_code = input("Código   : ")
      user_name = input("Nombre   : ")
      user_lastname = input("Apellido : ")
      user_age = input("Edad     : ")
      user_height = input("Estatura : ")
      user_blood_gr = input("Grp sang : ")
      user_blood_tp = input("Tip sang : ")
      user_is_activate = input("¿Activo? : ")
      print()

      # Consultar Usuarios
      print('\n' + ('-' * 82))
      print("Consultar Usuarios\n")
      print('+' + ('-' * 79) + '+')
      print('| Code\t\t| Nombre\t| Apellido\t| Edad\t| Estat\t| Sang\t| Est\t|')
      print('+' + ('-' * 79) + '+')
      print('| {}\t| {}\t| {}\t| {}\t| {}\t| {} {}\t| {}\t|'.format(_user_code, user_name,
            user_lastname, user_age, user_height, user_blood_gr, user_blood_tp, user_is_activate))
      print('+' + ('-' * 79) + '+\n')