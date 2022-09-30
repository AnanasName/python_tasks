def task1():
    digit = int(input())
    firstDigit = digit // 10
    secondDigit = digit % 10
    print(secondDigit, firstDigit)


def task2():
    digit = int(input())
    firstDigit = digit // 10
    secondDigit = digit % 10
    resultDigit = secondDigit * 10 + firstDigit
    print(resultDigit)


def task3():
    digit = int(input())
    print(digit % 100)


def task4():
    digit = int(input())
    print((digit % 100) // 10)


def task5():
    digit = int(input())
    sum = digit // 100 + (digit % 100) // 10 + digit % 10
    print(sum)


def task6():
    digit = float(input())
    firstDigit = int((digit % 1) // 0.1)
    print(firstDigit)


def task7():
    digit = int(input())
    print(int(-1 * digit // 100 * -1))


def task8():
    day = int(input())
    offset = 4
    print(day % 365 + offset - 1)


def task9():
    minuts = int(input())
    print(f"{minuts // 60}:{minuts % 60}")


def task10():
    a = int(input())
    b = int(input())
    c = int(input())

    print((a // 2 + a % 2) + (b // 2 + b % 2) + (c // 2 + c % 2))
