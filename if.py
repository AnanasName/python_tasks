def task1():
    number = int(input())
    if number % 2 == 0:
        print("Чёт")
    else:
        print("Нечёт")


def task2():
    number1 = int(input())
    number2 = int(input())
    if number1 < number2:
        print(number1)
    else:
        print(number2)


def task3():
    number = int(input())
    if number > 0:
        print(1)
    elif number == 0:
        print(0)
    else:
        print(-1)


def task4():
    number = int(input())
    if number > 99 or number < -99:
        print("Да")
    else:
        print("Нет")


def task5():
    number1 = int(input())
    number2 = int(input())
    if number1 > 0 or number2 > 0:
        print("Да")
    else:
        print("Нет")


def task6():
    number = int(input())

    if number // 100 < number // 10 % 10 < number % 10:
        print('Yes')
    else:
        print("No")


def task7():
    number = int(input())

    if number // 1000 == number % 10 and number // 100 % 10 == number // 10 % 10:
        print("Yes")
    else:
        print("No")


def task8():
    number = int(input())
    if number == 2:
        print('28')
    elif number in [1, 3, 5, 7, 8, 10, 12]:
        print("31")
    else:
        print('30')


def task9():
    x1, x2, x3 = int(input()), int(input()), int(input())
    if x1 == x2 == x3:
        print("3")
    elif x1 == x2 or x2 == x3 or x1 == x3:
        print("2")
    else:
        print("0")


def task10():
    x = int(input())
    y = int(input())

    if (x + y) % 2 == 0:
        print("Черная")
    else:
        print("Белая")


def task11():
    x1 = int(input())
    y1 = int(input())

    x2 = int(input())
    y2 = int(input())

    if (x1 + y1) % 2 == (x2 + y2) % 2:
        print("Да")
    else:
        print("Нет")


def task12():
    month = int(input())
    day = int(input())
    current_year = 2022

    months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day == months[month - 1]:
        if month == 12:
            print(f"1-1-{current_year + 1}")
        else:
            print(f"1-{month + 1}-{current_year}")
    else:
        print(f"{day + 1}-{month}-{current_year}")
