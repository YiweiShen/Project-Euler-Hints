from multiprocessing.pool import Pool

def cal_list(num):
    the_list = [1]
    st = 1
    interval = 2
    for i in range(num):
        for j in range(4):
            st += interval
            the_list.append(st)
        interval += 2
    return the_list


def cal_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num


def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True


def try_num(k):
    test_list = cal_list(k)
    num_range = test_list
    p = Pool(processes=16)
    check_list = p.map(is_prime, num_range)
    p.close()
    p.join()
    sum = 0
    for i in check_list:
        if i == True:
            sum += 1
    print(str(k)+':'+str(sum/len(test_list)))
    return sum/len(test_list)

for i in range(13100, 14000):
    if try_num(i) < 0.1:
        break

