import math


def function():
    pass


prime_list = []


def is_prime(num):
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    for i in range(2, 9999):
        if is_prime(i):
            prime_list.append(i)
            continue
        flag = 0
        for j in range(len(prime_list)):
            x = math.sqrt((i - prime_list[j])/2)
            if x == int(x):
                # print(i, prime_list[j], x)
                flag = 1
        if flag == 0 and i/2 != int(i/2):
            print(str(i)+'!!!')
