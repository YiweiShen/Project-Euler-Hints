# https://math.stackexchange.com/questions/886083/minimum-number-of-out-shuffles-required-to-get-back-to-the-start-in-a-pack-of-2
# http://oeis.org/A002326

# 2**60-1 == 3*3*5*5*7*11*13*31*41*61*151*331*1321

import math
from multiprocessing.pool import Pool
import time

start_time = time.time()

def cal_time(LEN):
    if pow(2, 60, LEN-1) == 1:
        return LEN
    return None

def double_cal_time(LEN):
    print(LEN)
    idx = 1
    t = 1
    while True:
        if idx < LEN/2:
            idx *= 2
        else:
            idx = 2*idx +1 - LEN
        if idx == 1:
            break
        else:
            t += 1
    if t == 60:
        return LEN
    return None

sort_num_range = range(2,10**4,2)
p = Pool(processes=100)
sort_list = p.map(cal_time, sort_num_range)
p.close()
p.join()
sort_list_clear = [x for x in sort_list if x is not None]
print(sort_list_clear)

num_range = sort_list_clear
p = Pool(processes=100)
result_list = p.map(double_cal_time, num_range)
p.close()
p.join()
result_list_clear = [x for x in result_list if x is not None]
print(result_list_clear)
print(sorted(list(set(sort_list_clear)-set(result_list_clear))))

print('time:'+str(time.time() - start_time))
