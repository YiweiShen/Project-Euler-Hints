import time


start_time = time.time()


def A(n):
    t = 0
    k = 1
    while k != 0:
        t += 1
        k = (10*k +1) % n
    return t

i = 1000001
while True:
    print(i)
    if pow(i,1,5) == 0:
        i += 2
    if A(i) > 10**6:
        print(i)
        break
    i += 2




print('time:'+str(time.time()-start_time))
