
import time
from multiprocessing.pool import Pool


t = time.time()


def cal_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num

def is_permutation(num1, num2):
    return sorted(list(str(num1))) == sorted(list(str(num2)))


num_range= range(2000,5000)
p = Pool(processes=16)
prime_list = p.map(cal_prime, num_range)
p.close()
p.join()
prime_list_clear = [x for x in prime_list if x is not None]
print(prime_list_clear)
min_num = 2
min_test_num = 3

for i in prime_list_clear:
    for j in prime_list_clear:
        test_num = i * j
        a = (i-1)*(j-1)
# We can reduce our search significantly by selecting prime pairs (p1, p2 ) and calculate n as n = p1 x p2. This allows the totient to be calculated as φ(n) = (p1-1)(p2-1) for n
        if test_num < 10000000:
            if is_permutation(a , test_num):
                if test_num / a < min_num:
                    min_num = test_num / a
                    print(test_num)
                    min_test_num = test_num
                    print('min_num:'+str(min_num))
print('min_ts:'+str(min_test_num))
print('time:'+str(time.time()-t))
