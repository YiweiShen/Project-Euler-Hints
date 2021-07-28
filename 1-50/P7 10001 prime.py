import math

pos=2

def is_prime(some_num):
    for a in range(2, int(math.sqrt(some_num))+1):
        if some_num % a == 0:
            return False
    return True


if __name__ == '__main__':
    for x in range(4, 99999999):
        if is_prime(x):
            pos += 1
            print('pos '+str(pos)+': '+str(x))
