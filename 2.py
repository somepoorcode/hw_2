n = int(input("Введите кол-во треугольников: "))
print()

for n in range(1, n + 1):
    triangle_size = 2 ** n
    for row in range(triangle_size-1, -1, -1):
        for i in range(row):
            print(" ", end="")

        for col in range(triangle_size):
            if col & row:
                print("  ", end="")
            else:
                print("* ", end="")
        print()
    print()