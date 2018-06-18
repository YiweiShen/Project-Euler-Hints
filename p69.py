from multiprocessing.pool import Pool
from multiprocessing import Manager


def phi(num):
    sum = 0
    for i in range(2, int(num*0.5+1)):
        if num % i == 0:
            sum += num/i - 1
    return num - sum - 1

manager = Manager()
result_dict = manager.dict()

def check(num):
    print(num)
    a = phi(num)
    if a:
        result_dict[num] = num / a

p = Pool(processes=16)
num_range= range(10**5*9,10**6)
p.map(check, num_range)
p.close()
p.join()

print(result_dict)

max_num = 1
max_n = 1

for i, j in result_dict.items():
    if j > max_num:
        max_n = i

print(max_n)

# damn too slow
