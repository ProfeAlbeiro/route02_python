'''
while True:
    print('\nSe ejecutó\n')
counter = 0
while (counter < 10):
    counter += 1
    print(counter)
counter = 0
while (counter < 20):
    counter += 1
    if (counter == 15):
        break
    print(counter)
'''
counter = 0
while (counter < 20):
    counter += 1
    if (counter < 15):
        continue
    print(counter)


print()
# While Loops
print("While Loops")
print()
print("     i = 1")
print("     while i <= 10:")
print("         print(i)")
print("         i += 1")
print()
i = 1
while i <= 10:
    print(i)
    i += 1
print()
print("     i = 10")
print("     while i > 0:")
print("         print(i)")
print("         i -= 1")
print()
i = 10
while i > 0:
    print(i)
    i -= 1

print()
