import time
from multiprocessing.pool import Pool
from decimal import Decimal

LIMIT = 10**9
start_time = time.time()

def check(num):
    print(num)
    num = Decimal(num)
    sum = 0
    a = (num*num - ((num-1)/2)**2)**Decimal(0.5) * (num-1)/2
    b = (num*num - ((num+1)/2)**2)**Decimal(0.5) * (num+1)/2
    if a == Decimal(int(a)):
        sum += 3*num - 1
        return sum
    if b == Decimal(int(b)):
        sum += 3*num + 1
    return sum

p = Pool(processes=16)
num_range = range(2, int(LIMIT/3)+1)
result_list = p.map(check, num_range)
p.close()
p.join()

print(sum(result_list))
print('time:'+str(time.time()-start_time))

# brute force anyway
# correct answer after 26324 seconds
