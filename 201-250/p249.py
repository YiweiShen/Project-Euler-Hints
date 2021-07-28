import itertools
from multiprocessing.pool import Pool
import time
import math


start_time = time.time()
the_list = []


def is_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True


for i in range(2,5000):
    if is_prime(i):
        the_list.append(i)

print(the_list)


def combo_num(n,r):
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r)) % 10**16

com_sum = 0
for i in range(1, len(the_list)+1):
    print(i)
    com_sum += i * combo_num(len(the_list), i)

r = pow(int(sum(the_list)*com_sum/len(the_list)), 1, 10**16)
print(r)


print('time:'+str(time.time()-start_time))
