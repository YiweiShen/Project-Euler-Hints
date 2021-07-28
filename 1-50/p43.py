import time
from multiprocessing.pool import Pool


def is_pandigital(num):
    if len(set(str(num))) == 10:
        return True
    return False


def check_divisibility(num):
    if int(str(num)[1:4]) % 2 == 0:
        if int(str(num)[2:5]) % 3 == 0:
            if int(str(num)[3:6]) % 5 == 0:
                if int(str(num)[4:7]) % 7 == 0:
                    if int(str(num)[5:8]) % 11 == 0:
                        if int(str(num)[6:9]) % 13 == 0:
                            if int(str(num)[7:10]) % 17 == 0:
                                return True
    return False

result_list = []

def check(num):
    print(num)
    global result_list
    if is_pandigital(num) and check_divisibility(num):
        result_list.append(num)


if __name__ == '__main__':
    t = time.time()
    num_range = range(1000000000, 10000000000)
    p = Pool(processes=100)
    p.map(check, num_range)
    p.close()
    p.join()
    print(sum(result_list))
    print('time:'+str(time.time()-t))
