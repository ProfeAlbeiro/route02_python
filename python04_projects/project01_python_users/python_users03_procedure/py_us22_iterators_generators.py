print()
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

print("Iterador y generador")
print()
print("     def fibonacci(max):")
print("         a, b = 0, 1")
print("         while a < max:")
print("             yield a")
print("             a, b = b, a+b")
print()
print()
fib1 = fibonacci(20)
fib_nums = [num for num in fib1]
print()
print("     fib1 = fibonacci(20)")
print("     fib_nums = [num for num in fib1]")
print("     print(fib_nums) =", fib_nums)
print()
double_fib_nums = [num * 2 for num in fib1]  # no va a funcionar
print("     double_fib_nums = [num * 2 for num in fib1]")
print("     print(double_fib_nums) =", double_fib_nums)
print()
double_fib_nums = [num * 2 for num in fibonacci(30)]  # sí funciona
print("     double_fib_nums = [num * 2 for num in fibonacci(30)]")
print("     print(double_fib_nums) =", double_fib_nums)

print()