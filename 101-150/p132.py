from multiprocessing.pool import Pool
import math


def cal_dividor(num):
    list_a = []
    i = 0
    while num > 1:
        if num % prime_list_clear[i] == 0:
            print(prime_list_clear[i])
            list_a.append(prime_list_clear[i])
            num /= prime_list_clear[i]
            continue
        i += 1
    return list_a


def cal_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num

p=Pool(processes=16)
num_range = range(2,1000000)
prime_list = p.map(cal_prime, num_range)
p.close()
p.join()
prime_list_clear = [x for x in prime_list if x is not None]
print(prime_list_clear)


count=0
result =0
i = 0
print(pow(10, 10**9, 9 * prime_list_clear[0]))
while (count<40):
    a = prime_list_clear[i] * 9
    if pow(10, 10**9, a) == 1:
        result += a /9
        count += 1
    i += 1

print(result)
