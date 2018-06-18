import time
from multiprocessing.pool import Pool


def is_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num

max_loop=0
max_loop_prime=0


if __name__ == '__main__':
    t = time.time()
    p = Pool(processes=16)

    num_range = range(2, 10**6)
    prime_list = p.map(is_prime, num_range)
    p.close()
    p.join()
    prime_list_clear = [x for x in prime_list if x is not None]

    print(prime_list_clear)
    print(len(prime_list_clear))

    for i in range(len(prime_list_clear)-1, -1, -1):
        print(i)
        print('max_loop_prime:'+str(max_loop_prime)) # never mind it's 997651
        for j in range(0, i):
            loop = 0
            sum = 0
            pos = j
            while True:
                sum += prime_list_clear[pos]
                loop += 1
                pos += 1
                if sum > prime_list_clear[i]:
                    break
                if sum == prime_list_clear[i]:
                    if loop > max_loop:
                        max_loop = loop
                        max_loop_prime = prime_list_clear[i]
                    break
                if loop > i-j:
                    break
    print(max_loop)
    print(max_loop_prime)
    print('time:'+str(time.time()-t))
