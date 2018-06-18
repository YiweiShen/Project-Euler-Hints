from multiprocessing.pool import Pool
import time

t =time.time()

def cal_prime(num):
    print(num)
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num


def is_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True


def cal_s(num):
    print(num)
    p1 = prime_list_clear[num]
    p2 = prime_list_clear[num+1]
    t = 1
    while True:
        test = t*10**(len(str(p1))) + p1
        if test % p2 == 0:
            return int(test)
        t += 1


p = Pool(processes=16)
num_range = range(5, 10**6+10)
prime_list = p.map(cal_prime, num_range)
p.close()
p.join()
prime_list_clear = [x for x in prime_list if x is not None]
print(prime_list_clear)

p = Pool(processes=16)
num_range = range(0, len(prime_list_clear)-1)
result_list = p.map(cal_s, num_range)
p.close()
p.join()
print(result_list)
print(sum(result_list))

print('time:'+str(time.time()-t))
# answer correct, too slow
