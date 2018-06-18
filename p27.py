import time
from multiprocessing.pool import Pool


def is_prime(num):
    print(num)
    for i in range(2, int(num**0.5 + 1)):
        if num % i == 0:
            return None
    return num


b_list = [x for x in range(2, 1001) if is_prime(x)]



def function_ab():
    global a_max
    global b_max
    global n_max
    for a in range(-1000, 1001):
        print(a)
        for b in b_list:
            n = 1
            while True:
                test_num = n * n + a * n + b
                if test_num not in prime_list_clear:
                    break
                n += 1
            if n - 1 > n_max:
                a_max = a
                b_max = b
                n_max = n - 1
                print('n_max:'+str(n_max))
    return n_max


if __name__ == '__main__':
    n_max = 0
    a_max = 0
    b_max = 0

    t = time.time()


    p = Pool(processes=100)
    nums_prime = range(2, 10**6)
    prime_list = p.map(is_prime, nums_prime)
    p.close()
    p.join()
    prime_list_clear = [x for x in prime_list if x is not None]
    print(prime_list_clear)
    function_ab()
#    p = Pool(processes=100)
#    nums_quadratic = range(-1000, 1001)
#    result_list = p.map(function_ab, nums_quadratic)
#    print(result_list)
    print(a_max*b_max)


    print('time:' + str(time.time() - t))
