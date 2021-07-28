from multiprocessing.pool import Pool
import time


start_time = time.time()

def cal_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num


def is_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True

def is_concatenate(num1, num2):
    if is_prime(int(str(num1)+str(num2))) and is_prime(int(str(num2)+str(num1))):
        return 1
    return 0


p = Pool(processes=16)
num_range = range(2,10**6)
prime_list = p.map(cal_prime, num_range)
p.close()
p.join()
prime_list_clear = [x for x in prime_list if x is not None]
print(prime_list_clear)


check_list = []

for i in prime_list_clear:
    print(i)
    check_list.append([i])
    for x in check_list:
        check_s = 0
        for j in range(len(x)):
            check_s += is_concatenate(i, x[j])
        if check_s == len(x):
            check_list.append(x+[i])
            if len(check_list[-1]) == 4:
                print(check_list[-1])
            if len(check_list[-1]) == 5:
                print(check_list[-1])
                print('time:'+str(time.time()-start_time))
                quit()

# it took 1500s to find the first five prime set, and in fact, it is not necesarily the least sum maybe but it is the correct answer.
