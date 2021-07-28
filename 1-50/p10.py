import math

sum = 0

def is_prime(some_num):
    for a in range(2, int(math.sqrt(some_num)) + 1):
        if some_num % a == 0:
            return False
    return True


if __name__ == '__main__':
    for a in range(2, 2000000):
        if is_prime(a):
            sum += a
    print(sum)
