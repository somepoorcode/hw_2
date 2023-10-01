from math import factorial
n = int(input("Введите натуральное число: "))

for i in range(0, n):
    for j in range(n - i + 1):
        print(end=" ")

    for j in range(0, i + 1):
        numbers = (factorial(i) // (factorial(j) * factorial(i-j)))

        print(str(numbers), end=" ")

    print()