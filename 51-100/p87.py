import time
from multiprocessing.pool import Pool


def is_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num


if __name__ == '__main__':
    t = time.time()
    p1 = Pool(processes=30)
    p2 = Pool(processes=30)
    p3 = Pool(processes=30)
    num1 = range(2, 7072)
    num2 = range(2, 369)
    num3 = range(2, 85)
    prime_list1 = p1.map(is_prime, num1)
    p1.close()
    p1.join()
    prime_list2 = p2.map(is_prime, num2)
    p2.close()
    p2.join()
    prime_list3 = p3.map(is_prime, num3)
    p3.close()
    p3.join()
    prime_list1_clear = [x for x in prime_list1 if x is not None]
    prime_list2_clear = [x for x in prime_list2 if x is not None]
    prime_list3_clear = [x for x in prime_list3 if x is not None]

    result_list = []
    for i in prime_list1_clear:
        print(i)
        for j in prime_list2_clear:
            for k in prime_list3_clear:
                test_num = i**2 + j**3 + k**4
                if test_num < 50000000:
                    result_list.append(test_num)
    print(str(len(list(set(result_list)))))
    print('time:'+str(time.time()-t))
