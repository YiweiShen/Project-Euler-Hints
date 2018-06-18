def is_palindromic(some_number):
    return some_number == reverse_num(some_number)


def reverse_num(some_number):
    list_number = list(reversed(str(some_number)))
    return int(''.join(list_number))


if __name__ == '__main__':
    for x in range(999, 100, -1):
        for y in range(999, 100, -1):
            if is_palindromic(x * y):
                print(x * y)


#then you have to find the max of number, anyway i just looked at it
