def loops():
    for i in range(1, 21, 2):
        print(i, end=' ')
    print()

    for i in range(0, 110, 10):
        print(i, end=' ')
    print()

    for x in range(20, 0, -1):
        print(x, end=' ')
    print()

    w = int(input("How many stars do you want to print:"))
    for n in range(0, w):
        print("*", end=' ')
    print()

    for n in range(1, w + 1):
        print("*" * n)


loops()
