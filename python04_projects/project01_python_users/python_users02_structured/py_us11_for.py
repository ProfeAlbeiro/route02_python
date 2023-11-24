'''
for element in range(20):
    print(element)
for element in range(1, 21):
    print(element)
'''
my_list = [23, 45, 67, 89, 43]
for element in my_list:
    print(element)
my_tuple = ('nico', 'juli', 'santi')
for element in my_tuple:
    print(element)
product = {
    'name': 'Camisa',
    'price': 100,
    'stock': 89,
}
for key in product:
    print(key, '=>', product[key])
for key, value in product.items():
    print(key, '=>', value)
people = [
    {
        'name': 'nico',
        'age': 34
    },
    {
        'name': 'zule',
        'age': 45
    },
    {
        'name': 'santi',
        'age': 32
    }
]
for person in people:
    print(person)
for person in people:
    print('name =>', person['name'])

    print()
# For Loops
print("Foor Loops")
print()
# range()
print("Rango: range()")
print()
print("     print(range(10))=", range(10))
print()
print("     for i in range(10):")
print("         print(i)")
print()
for i in range(10):
    print(i)

print()
