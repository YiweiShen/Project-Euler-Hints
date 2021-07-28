import time


def is_prime(num):
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True


def is_truncatable(num, plist):
    for i in range(1, len(str(num))):
        if int(str(num)[i:]) not in plist:
            return False
        if int(str(num)[:-i]) not in plist:
            return False
    return True

if __name__ == '__main__':
    t = time.time()
    prime_list = []
    for i in range(2, 10**6):
        if is_prime(i):
            prime_list.append(i)
    print(prime_list)
    for i in prime_list:
        if is_truncatable(i, prime_list):
            print(i)

    print('time:'+str(time.time()-t))
