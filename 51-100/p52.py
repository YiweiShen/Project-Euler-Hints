def check(some_num):
    l = sorted(list(set(str(some_num))))
    if l == sorted(list(str(some_num*2))):
        if l == sorted(list(str(some_num*3))):
            if l == sorted(list(str(some_num*4))):
                if l == sorted(list(str(some_num*5))):
                    return l == sorted(list(str(some_num*6)))
    return False


if __name__ == '__main__':
    for i in range(1, 9999999):
        if check(i):
            print(i)

