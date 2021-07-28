from multiprocessing.pool import Pool
import time


start_time = time.time()

def is_square(n):
    return n**0.5 == int(n**0.5)


def n_check(n):
    if not (n % 4 ==0):
        return 0
    print(n)
    sum = 0
    for i in range(int(n**0.5)+1, int(n/4)+2):
        if is_square(i*i-n):
            if (i*i-n)**0.5 % 2 == i % 2:
                sum += 1
    return sum


p = Pool(processes=8)
num_range = range(1, 10**6+1)
result_list = p.map(n_check, num_range)
p.close()
p.join()

test = 0
result = 0

for i in result_list:
    if 1<=i<=10:
        result += 1
    if i ==15:
        test += 1

print('N(15)='+str(test))
print('Final:'+str(result))

print('time:'+str(time.time()-start_time))
