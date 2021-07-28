import itertools
from multiprocessing.pool import Pool
import time
import math


start_time = time.time()
NUM_LIMIT = 4999
the_set = set()


def is_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True


for i in range(2,NUM_LIMIT+1):
    if is_prime(i):
        the_set.add(i)

print(the_set)

the_list = [0]

for i in range(1, NUM_LIMIT+1):
    the_list.append(pow(i,i,10**16))


def find_product(i):
    print(i)
    product = 1
    for j in range(NUM_LIMIT-i+1, NUM_LIMIT+1):
        product *= j
    return product//math.factorial(i)



# def check(num):
#     sum = 0
#     print(num)
#     d = set(itertools.combinations(the_set,num))
#     for j in d:
#         for k in j:
#             sum += the_list[k]
#     return sum



p = Pool(processes=8)
num_range = range(1, NUM_LIMIT+1)
result_list = p.map(find_product, num_range)
p.close()
p.join()

print(sum(result_list))

# final_sum = sum(result_list) % 10**16
# print(final_sum)

print('time:'+str(time.time()-start_time))
