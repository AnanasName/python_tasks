def task1():
    print(input().count(' ') + 1)


def task2():
    strings = input().split(' ')
    print(strings[1], strings[0])


def task3():
    inp = input()
    parts = inp.split('f')
    if len(parts) == 1:
        print(-1)
    elif len(parts) == 2:
        print(len(parts[0]))
    else:
        print(f"{len(parts[0])} {len(inp) - len(parts[-1]) - 1}")


def task4():
    print(input().replace('1', 'one'))


def task5():
    print(input().replace('@', ''))
