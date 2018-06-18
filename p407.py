import time
from multiprocessing.pool import Pool


start_time = time.time()
NUM_LIMIT = 10**7

def M(n):
    for i in range(n, 0, -1):
        if pow(i,2,n)  == i:
            print(str(n)+':'+str(i))
            return i
    return 0


p=Pool(processes=8)
num_range = range(1, NUM_LIMIT+1)
result_list = p.map(M, num_range)
p.close()
p.join()

print(sum(result_list))

print('time:'+str(time.time()-start_time))
