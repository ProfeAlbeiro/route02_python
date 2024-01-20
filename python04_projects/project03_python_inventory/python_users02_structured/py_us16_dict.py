my_dict = {}
print(type(my_dict))
my_dict = {
    'avion': "bla bla bla",
    'name': "Nicolás",
    'last_name': "Molina Monroy",
    'age': 87
}
print(my_dict)
print(len(my_dict))
print(my_dict['age'])
print(my_dict['last_name'])
print(my_dict.get('age'))
print(my_dict.get('unvalor'))
print('avion' in my_dict)
print('otroqueno' in my_dict)

person = {
    'name': 'nico',
    'last_name': 'molina',
    'langs': ['python', 'javascript'],
    'age': 99,
}
print(person)

# Actualización
person['name'] = 'Santi'
person['age'] -= 50
person['langs'].append('rust')
print(person)
# Eliminar
del person['last_name']
person.pop('age')
print(person)
# items, keys, values
print('items')
print(person.items())
print('keys')
print(person.keys())
print('values')
print(person.values())


print()
# Listas
print(40*"*", "Diccionarios", 40*"*")
print()
rae = {}
rae['pizza'] = 'Comida rápida triangular'
rae['pasta'] = 'Comida popular italiana'
print("     rae = {}")
print("     rae['pizza'] = 'Comida rápida triangular'")
print("     rae['pasta'] = 'Comida popular italiana'")
print()
print("     print(rae) =", rae)
print()
# Conocer el Valor de un diccionario
print("Conocer el Valor de un diccionario")
print()
print("     print(rae['pizza']) =", rae['pizza'])
print()
# get() : Manejo de errores en un diccionario
print("get() : Manejo de errores en un diccionario")
print()
a = rae.get('helado', None)
print("     a = rae.get('helado', None)")
print("     print(a) =", a)
print()
a = rae.get('pizza', None)
print("     a = rae.get('pizza', None)")
print("     print(a) =", a)
print()
# keys() : Devuelve las llaves de un diccionario
print("keys() : Devuelve las llaves de un diccionario")
print()
print("     print(rae.keys()) =", rae.keys())
print()
# values() : Devuelve los valores de un diccionario
print("values() : Devuelve los valores de un diccionario")
print()
print("     print(rae.values()) =", rae.values())
print()
# items() : Devuelve tuplas (llave, valor) de un diccionario
print("items() : Devuelve tuplas (llave, valor) de un diccionario")
print()
print("     print(rae.items()) =", rae.items())
print()
# Iterar diccionarios
print(36*"*", "Iterar diccionarios", 36*"*")
print()
# Iterar Llaves : keys()
print("Iterar Llaves : keys()")
print()
print("     for key in rae.keys():")
print("         print(key)")
print()
for key in rae.keys():
    print("    ", key)

print()
# Iterar Valores : values()
print("Iterar Valores : values()")
print()
print("     for value in rae.values():")
print("         print(value)")
print()
for value in rae.values():
    print("    ", value)

print()
# Iterar Tuplas (llave, valor) : items()
print("Iterar Tuplas (llave, valor) : items()")
print()
print("     for key, value in rae.items():")
print("         print(key,", "\' : \',", "value)")
print()
for key, value in rae.items():
    print("    ", key, ' : ', value)

print()

print()
