def read_int_sequence():
    sequence = [int(number) for number in input().split()]
    return sequence


def task1():
    seq = read_int_sequence()
    for number in seq:
        if number % 2 == 1:
            print(number, end=' ')


def task2():
    seq = read_int_sequence()
    for i, number in enumerate(seq):
        if i == 0:
            continue
        if number > seq[i - 1]:
            print(number, end=' ')


def task3():
    seq = read_int_sequence()
    for i, n in enumerate(seq):
        if i % 2 == 1:
            print(n, seq[i - 1], end=' ')

    if len(seq) % 2 == 1:
        print(seq[-1])


def task4():
    seq = read_int_sequence()
    max_digit, max_index = seq[0], 0
    min_digit, min_index = seq[0], 0

    for i, n in enumerate(seq):
        if n > max_digit:
            max_digit = n
            max_index = i
        elif n < min_digit:
            min_digit = n
            min_index = i

    seq[max_index], seq[min_index] = seq[min_index], seq[max_index]
    print(seq)


def task5():
    seq1 = read_int_sequence()
    seq2 = read_int_sequence()

    count = 0
    for first_digit in seq1:
        for second_digit in seq2:
            if first_digit == second_digit:
                count += 1

    print(count)


def task6():
    seq1 = read_int_sequence()
    seq2 = read_int_sequence()

    seq1.sort()
    seq2.sort()

    for first_digit in seq1:
        for second_digit in seq2:
            if first_digit == second_digit:
                print(first_digit, end=' ')
            elif second_digit > second_digit:
                break

    print()


def task7():
    seq = read_int_sequence()

    for digit, n in enumerate(seq):
        seen = False
        for digit in range(digit - 1, 0, -1):
            if seq[digit] == n:
                print("ДА")
                seen = True
                break

        if not seen:
            print("НЕТ")


def task8():
    stroke = input()

    print(stroke[2])
    print(stroke[-1])
    print(stroke[:5])
    print(stroke[:-2])
    [(print(n, end='') if i % 2 == 0 else 0) for i, n in enumerate(stroke)]
    print()
    [(print(n, end='') if i % 2 == 1 else 0) for i, n in enumerate(stroke)]
    print()
    print(stroke[::-1])
    [(print(n, end='') if i % 2 == 0 else 0) for i, n in enumerate(stroke[::-1])]
    print()


def task9():
    stroke = input()
    mid = len(stroke) // 2 + len(stroke) % 2
    print(f'{stroke[mid:]}{stroke[:mid]}')


def task10():
    s = input()

    leftIdx = s.index('h')
    rightIdx = s[::-1].index('h')

    print(f'{s[:leftIdx]}{s[(len(s) - rightIdx):]}')


def task11():
    stroke = input()

    left_index = stroke.index('h')
    right_index = stroke[::-1].index('h')

    print(f'{stroke[:left_index]}{stroke[(len(stroke) - right_index - 1):(left_index - 1):-1]}{stroke[(len(stroke) - right_index):]}')


def task12():
    stroke = input()

    left_index = stroke.index('h')
    right_index = stroke[::-1].index('h')
    changed_stroke = stroke[left_index + 1:len(stroke) - right_index - 1].replace('h', 'H')
    print(f'{stroke[:left_index + 1]}{changed_stroke}{stroke[len(stroke) - right_index - 1:]}')
