# Proceso1: Se importa una librería
import random
# Proceso2: Se colocan opciones en una tupla
options = ('piedra', 'papel', 'tijera')
# Iniciar variables
computer_wins = 0
user_wins = 0
rounds = 1
# Proceso3: se repite hasta que el usuario o la computadora gane
while True:
    # Salida de Datos:
    print()
    print('*' * 10)
    print('ROUND', rounds)
    print('*' * 10)
    print('\ncomputer_wins', computer_wins)
    print('user_wins', user_wins)
    # Entrada de datos    
    user_option = input('\nPiedra, papel o tijera: ')
    # Proceso4: Se cambia a minúsculas
    user_option = user_option.lower()
    # Proceso5: Se acumula la cantidad de encuentros
    rounds += 1
    # Proceso6: Si la opción del usuario NO es válida, entonces imprime ¡Esa opción no es válida!
    print()
    if not user_option in options:
        # Salida de datos
        print('Esa opción NO es válida')
        # Sale de la condicional y continúa con las otras opciones
        continue    
    # Proceso7: Se elige de la tupla un valor aleatorio
    computer_option = random.choice(options)
    # Salida de datos
    print('User option => ', user_option)
    print('Computer option => ', computer_option)
    # Proceso8: 
    # 8.1. Si la opción es igual a la computadora, entonces imprime ¡Empate!
    if (user_option == computer_option):
        print('¡Empate!')            
    # 8.2. Si la opción del usuario es piedra, entonces queda evaluar tijera o papel con la computadora
    elif (user_option == 'piedra'):
        # 8.2.1. Si la opción de la computadora es tijera, entonces ¡user ganó!
        if (computer_option == 'tijera'):
            print('\npiedra gana a tijera')
            print('\n¡user ganó!')
            # Se acumula cuando el usuario gana
            user_wins += 1
        # 8.2.2. Si la opción de la computadora es papel, entonces ¡computer ganó!
        else:
            print('\npapel gana a piedra')
            print('\ncomputer ganó!')
            # Se acumula cuando la computadora gana
            # Se acumula cuando la computadora gana
            computer_wins += 1
    # 8.3. Si la opción del usuario es papel, entonces queda evaluar piedra o tijera con la computadora
    elif (user_option == 'papel'):
        # 8.3.1. Si la opción de la computadora es piedra, entonces ¡user ganó!
        if (computer_option == 'piedra'):
            print('\npapel gana a piedra')
            print('\nuser ganó!')
            # Se acumula cuando el usuario gana
            user_wins += 1
        # 8.3.2. Si la opción de la computadora es tijera, entonces computer ganó!
        else:
            print('\ntijera gana a papel')
            print('\ncomputer ganó!')
            # Se acumula cuando la computadora gana
            computer_wins += 1
    # 8.4. Si la opción del usuario es tijera, entonces queda evaluar piedra o papel con la computadora
    elif (user_option == 'tijera'):
        # 8.4.1. Si la opción de la computadora es papel, entonces ¡user ganó!
        if (computer_option == 'papel'):
            print('\ntijera gana a papel')
            print('\nuser ganó!')
            # Se acumula cuando el usuario gana
            user_wins += 1
        else:
        # 8.4.2. Si la opción de la computadora es tijera, entonces ¡user ganó!
            print('\npiedra gana a tijera')
            print('\ncomputer ganó!')
            # Se acumula cuando la computadora gana
            computer_wins += 1
    # 8.5. Si el usuario obtiene dos victorias gana y termina el programa
    if (user_wins == 2):
        print('\nEl ganador es el usuario\n')
        # Sale de ciclo while
        break
    # 8.6. Si la computadora obtiene dos victorias gana y termina el programa
    if (computer_wins == 2):
        print('\nEl ganador es la computadora\n')
        # Sale de ciclo while
        break