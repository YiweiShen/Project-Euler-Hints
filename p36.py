def is_palindromic(num):
    return str(num) == str(num)[::-1]


def cal_binary(num):
    return str(bin(num))[2:]


if __name__ == '__main__':
    sum = 0
    for i in range(1, 1000000):
        print(i)
        if is_palindromic(i) and is_palindromic(cal_binary(i)):
            sum += i
    print(sum)
