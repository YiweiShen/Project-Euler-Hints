from time import time
from multiprocessing.pool import Pool


NUM_LIMIT = 1000000
start_time = time()


def cal_uv(i):
    print(i)
    result_list =[]
    for u in range(1, i):
        v = i/u
        if v < 1:
            continue
        if not (u+v) % 4:
            z_4 = 3*v-u
            if z_4> 0 and not z_4 % 4:
                result_list.append(1)
                if sum(result_list)>10:
                    return 11
    return sum(result_list)


def check(i):
    if cal_uv(i) == 10:
        return 1
    return 0

# test
assert cal_uv(1155) == 10
assert cal_uv(20) == 1

p = Pool(processes=8)
num_range = range(1, NUM_LIMIT+1)
result = p.map(check, num_range)
p.close()
p.join()


print(sum(result))

print('time:'+str(time()-start_time))

# slow but correct maybe
