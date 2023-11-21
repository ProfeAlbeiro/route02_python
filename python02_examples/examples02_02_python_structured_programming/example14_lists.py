import random
import copy
numbers = [1, 2, 3, 4]
print(numbers)
print(type(numbers))
tasks = ['make a dishes', 'play videogames']
print(tasks)
types = [1, True, 'hola']
print(types)
print(numbers[0])
print(tasks[0])
text = 'hola'
# text[0] = 'w' # Error
tasks[0] = 'watch platzi courses'
print(tasks)
tasks[0] = 'do the dishes'
print(tasks)
print(numbers[:3])
print(True in types)
print('hola' in types)


print()
# Listas
print(40*"*", "Listas", 40*"*")
print()
countries = ['Mexico', 'Venezuela', 'Colombia', 'Argentina']
ages = [12, 18, 24, 34, 50]
receta = ['Ensalada', 2, 'Lechuga', 5, 'Tomates']
print("     countries = ['Mexico','Venezuela','Colombia','Argentina']")
print("     ages = [12,18,24,34,50]")
print("     receta = ['Ensalada',2,'Lechuga',5,'Tomates']")
print()
print("     print(countries) =", countries)
print("     print(ages) =", ages)
print("     print(receta) =", receta)
print()
# Cambiar valor de una lista
print("Cambiar valor de una lista")
print()
countries[0] = 'Ecuador'
print("     countries[0] = 'Ecuador'")
print("     print(countries) =", countries)
print()
# Clonar una lista
print("Alias: Clonar una lista")
print()
global_countries = countries
countries[0] = 'Guatemala'
print("     global_countries = countries")
print("     countries[0] = 'Guatemala'")
print()
print("     print(countries) =", countries)
print("     print(global_countries) =", global_countries)
print()
# Copiar una lista
print("Copiar una lista")
print()
print("     import copy. Importar librería copy al principio del archivo")
print()
global_countries = None
global_countries = copy.copy(countries)
countries[0] = 'Honduras'
print("     global_countries = None")
print("     global_countries = copy.copy(countries)")
print("     countries[0] = 'Honduras'")
print()
print("     print(countries) =", countries)
print("     print(global_countries) =", global_countries)
print()
# Imprimir una lista
print("Imprimir una lista")
print()
print("     for country in countries:")
print("         print(country)")
print()
for country in countries:
    print("     ", country)

print()
# Operaciones con listas
print(31*"*", "Operaciones con listas", 32*"*")
print()
a = list(range(0, 20, 2))
b = list(range(0, 10))
fruits = list()
random_numbers = []
print("     a = list(range(0,20,2))")
print("     b = list(range(0,10))")
print("     fruits = list()")
print("     random_numbers = []")
print()
print("Sumar listas")
print()
print("     print(a + b) =", a + b)
print()
print("Multiplicar listas")
print()
print("     print(b * 2) =", b * 2)
print()
print("append() : Agregar elemento al final de una lista")
print()
fruits.append('apple')
fruits.append('banana')
fruits.append('kiwi')
fruits.append('manzana')
print("     fruits.append('apple')")
print("     fruits.append('banana')")
print("     fruits.append('kiwi')")
print("     fruits.append('manzana')")
print("     print(fruits) =", fruits)
print()
print("len()    : Tamaño de una lista")
print()
print("     print(len(fruits)) =", len(fruits))
print()
print("pop()    : Extraer elemento de una lista")
print()
some_fruit = fruits.pop()
print("     some_fruit = fruits.pop()")
print("     print(some_fruit) =", some_fruit)
print("     print(fruits) =", fruits)
print()
other_fruit = fruits.pop(1)
print("     other_fruit = fruits.pop(1)")
print("     print(other_fruit) =", other_fruit)
print("     print(fruits) =", fruits)
print()
print("del      : Eliminar elementos de una lista")
print()
del fruits[0]
print("     del fruits[0]")
print("     print(fruits) =", fruits)
print()
print("sorted() : Ordenar elementos sin afectar la lista")
print()
print("     import random. Importar librería random al principio del archivo")
print()
for i in range(10):
    random_numbers.append(random.randint(0, 15))

print("     for i in range(10):")
print("         random_numbers.append(random.randint(0,15))")
print()
print("     print(random_numbers) =", random_numbers)
ordered_numbers = sorted(random_numbers)
print()
print("     ordered_numbers = sorted(random_numbers)")
print()
print("     print(ordered_numbers) =", ordered_numbers)
print("     print(random_numbers) =", random_numbers)
print()
print("sort()   : Ordenar elementos afectando la lista")
print()
random_numbers.sort()
print("     random_numbers.sort()")
print("     print(random_numbers) =", random_numbers)
print()
print("dir()   : Conocer los métodos aplicables a una lista")
print()
print("     print(dir(random_numbers)) =", dir(random_numbers))


print()
