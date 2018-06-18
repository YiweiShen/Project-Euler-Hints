from multiprocessing.pool import Pool
import time

start_time = time.time()

def cal_time(LEN):
    global result_list
    print(LEN)
    idx = 1
    t = 1
    while True:
        if idx < LEN/2:
            idx *= 2
        else:
            idx = 2*idx +1 - LEN
        if idx == 1:
            break
        else:
            t += 1
    if t == 60:
        return LEN
    return None

num_range = range(2,1000,2)
p = Pool(processes=100)
result_list = p.map(cal_time, num_range)
p.close()
p.join()
result_list_clear = [x for x in result_list if x is not None]
print(result_list_clear)
print('time:'+str(time.time() - start_time))
# for i in range(2,1000000,2):
#     test_time = cal_time(i)
#     print(str(i)+':'+str(test_time))
#     if test_time == 60:
#         sum += i
#         print('sum::::::::::'+str(sum))


