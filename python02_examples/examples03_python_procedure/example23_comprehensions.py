import random
print()
# List comprehension
print(30*"*", "List comprehension", 30*"*")
print()
lista_numeros = list(range(100))
print("     lista_numeros = list(range(100))")
print()
print("     print(lista_numeros) =", lista_numeros)
print()
print()
print("Ejemplo_01   : Números pares")
print()
pares = [numero for numero in lista_numeros if numero % 2 == 0]
print("     pares = [numero for numero in lista_numeros if numero % 2 == 0]")
print()
print("     print(pares) =", pares)
print()
print()
# Dictionary comprehension
print(30*"*", "Dictionary comprehension", 30*"*")
print()
student_uid = [1, 2, 3]
students = ['Juan', 'José', 'Pedro']
students_with_uid = {uid: student for uid, student in zip(student_uid, students)}
print("     student_uid = [1, 2, 3]")
print("     students = ['Juan', 'José', 'Pedro']")
print()
print()
print("Ejemplo_01   : Unir los uid con los estudiantes")
print()
print("     students_with_uid = {uid: student for uid, student in zip(student_uid, students)}")
print()
print("     print(students_with_uid) =", students_with_uid)
print()
print()
# Set comprehension
print(30*"*", "Set comprehension", 30*"*")
print()
print("     import random (Dejarlo al principio de la página)")
print()
random_numbers = []
for i in range(10) :
    random_numbers.append(random.randint(1,3))

print("     random_numbers = []")
print()
print("     for i in range(10) :")
print("         random_numbers.append(random.randint(1,3))")
print()
print("     print(random_numbers) =", random_numbers)
print()
print()
print("Ejemplo_01   : Eliminar los números repetidos")
print()
non_repeated = {number for number in random_numbers}
print("     non_repeated = {number for number in random_numbers}")
print()
print("     print(non_repeated) =", non_repeated)


print()


print()