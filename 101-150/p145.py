from multiprocessing.pool import Pool
import time

t = time.time()

def is_reversible(num):
    print(num)
    if num % 10 == 0:
        return 0
    sum = num + int(str(num)[::-1])
    for i in str(sum):
        if int(i) % 2 == 0:
            return 0
    return 1


reversible_list = []

num_range = range(10**7)
p = Pool(processes=8)
reversible_list = p.map(is_reversible, num_range)
p.close()
p.join()

a = sum(reversible_list)



print('result:'+str(20*30**3+a))

print('time:'+str(time.time()-t))
