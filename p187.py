from multiprocessing.pool import Pool


def cal_prime(num):
    print(num)
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num


p = Pool(processes=16)
num_range = range(2, int(10**8/2))
prime_list = p.map(cal_prime, num_range)
p.close()
p.join()
prime_list_clear = [x for x in prime_list if x is not None]
print(prime_list_clear)

result_list = []

for i in range(0, len(prime_list_clear)):
    for j in range(i, len(prime_list_clear)):
        a = prime_list_clear[i]*prime_list_clear[j]
        print(a)
        if a > 10**8:
            break
        result_list.append(a)

result_list_check = list(set(result_list))

print(len(result_list_check))
# this takes too long and too much power to solve the problem
# however the result is right
