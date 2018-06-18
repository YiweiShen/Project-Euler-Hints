import math
from multiprocessing.pool import Pool


def find_next(num):
    sum = 0
    num_as_string = str(num)
    for i in num_as_string:
        sum += math.factorial(int(i))
    return sum


def check(num):
    print(num)
    the_list =[]
    k = num
    while k not in the_list:
        the_list.append(k)
        k = find_next(k)
    return len(the_list)


p = Pool(processes=16)
num_range = range(1, 10**6)
result_list = p.map(check, num_range)
p.close()
p.join()

result_sum = 0
for a in result_list:
    if a == 60:
        result_sum += 1

print(result_sum)
