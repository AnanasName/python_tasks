def read_str_sequence():
    sequence = [str(element) for element in input().split()]
    return sequence


def task1():
    words_dict = dict()
    words = read_str_sequence()
    for word in words:
        if word in words_dict:
            words_dict[word] += 1
            print(words_dict[word], end=' ')
        else:
            words_dict[word] = 0
            print(words_dict[word], end=' ')


def task2():
    syn_dict = dict()
    count = int(input())
    for i in range(count):
        syn_couple = read_str_sequence()
        syn_dict[syn_couple[1]] = syn_couple[0]
    syn = input()
    print(syn_dict[syn])


def task3():
    count = int(input())
    votes_dict = dict()
    names = set()
    for i in range(count):
        vote_couple = read_str_sequence()
        name = vote_couple[0]
        names.add(name)
        votes = int(vote_couple[1])
        if name in votes_dict:
            votes_dict[name] += votes
        else:
            votes_dict[name] = votes

    sorted(names, key=str)

    for name in names:
        print(f'{name} {votes_dict[name]}')


def task4():
    count = int(input())
    words_dict = dict()
    max_freq = 0
    result_word = ""
    for i in range(count):
        words = read_str_sequence()
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 0

    for word in sorted(words_dict.keys()):
        if words_dict[word] > max_freq:
            max_freq = words_dict[word]
            result_word = word

    print(result_word)


def task5():
    read_set = set()
    write_set = set()
    execute_set = set()
    count = int(input())

    for i in range(count):
        stroke = read_str_sequence()
        file_name = stroke[0]
        for j in range(1, stroke.__len__()):
            current_operation = stroke[j].lower()
            add_to_req_set("r", current_operation, read_set, file_name)
            add_to_req_set("x", current_operation, execute_set, file_name)
            add_to_req_set("w", current_operation, write_set, file_name)

    count = int(input())

    for i in range(count):
        stroke = read_str_sequence()
        operation = stroke[0]
        file_name = stroke[1]
        check_set("read", operation, read_set, file_name)
        check_set("write", operation, write_set, file_name)
        check_set("execute", operation, execute_set, file_name)


def add_to_req_set(check_operation_symbol, operation, operation_set, file_name):
    if operation == check_operation_symbol:
        operation_set.add(file_name)


def check_set(check_operation, operation, operation_set, file_name):
    if operation == check_operation:
        if operation_set.__contains__(file_name):
            print("OK")
        else:
            print("Denied")


def task6():
    count = int(input())
    city_dict = dict()
    for i in range(count):
        stroke = read_str_sequence()
        country = stroke[0]
        for j in range(1, stroke.__len__()):
            city_dict[stroke[j]] = country

    count = int(input())
    for i in range(count):
        city = input()
        print(city_dict[city])


def task7():
    count = int(input())
    words_dict = dict()
    for i in range(count):
        words = read_str_sequence()
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

    for value in sorted(words_dict.values(), reverse=True):
        for word in words_dict.keys():
            if words_dict[word] == value:
                print(word, end=" ")
                print(value)
                words_dict.pop(word)
                break
