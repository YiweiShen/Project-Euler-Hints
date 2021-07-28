import math
from multiprocessing.pool import Pool


def check(num):
    if num == 7:
        return 0
    a = int(num*3/7)
    while True:
        if a < 1:
            low = 0
            break
        if math.gcd(a, num) == 1:
            low = a
            break
        a -= 1
    return low


p = Pool(processes=16)
num_range = range(1,10**6)
result_list = p.map(check, num_range)
p.close()
p.join()

print(result_list)
min_n = 10
key_num = 0
for i in range(len(result_list)):
    if result_list[i] == 0:
        continue
    b = 3/7 - result_list[i]/(i+1)
    if b < min_n:
        min_n = b
        key_num = i+1

print(min_n)
print(key_num)
print(result_list[key_num-1])
