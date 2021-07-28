import time
from multiprocessing.pool import Pool


def is_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num

def is_different(num):
    return len(set(str(num))) == 3    # when it equals 4 produces 1487


def is_common(num1,num2,num3):
    return len(set(str(num1)+str(num2)+str(num3))) == 3


if __name__ == '__main__':
    t = time.time()
    p = Pool(processes=16)

    num = range(1000, 9999)

    prime_list = p.map(is_prime, num)
    p.close()
    p.join()

    prime_list_clear = [x for x in prime_list if x is not None]
    print(prime_list_clear)

    for i in range(0, len(prime_list_clear)):
        for j in range(i+1, len(prime_list_clear)):
            x = prime_list_clear[j] - prime_list_clear[i]
            if prime_list_clear[j]+x in prime_list_clear:
                if is_different(prime_list_clear[i]) and is_different(prime_list_clear[j]) and is_different(prime_list_clear[j]+x):
                    if is_common(prime_list_clear[i],prime_list_clear[j],prime_list_clear[j]+x):
                        print(prime_list_clear[i])
                        print(prime_list_clear[j])

    print('time:'+str(time.time()-t))
