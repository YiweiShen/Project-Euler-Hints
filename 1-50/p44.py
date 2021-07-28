from multiprocessing.pool import Pool


def cal_pentagonal(num):
    return int(num*(3*num - 1)/2)


p=Pool(processes=16)
num_range = range(1, 10**4)
pentagonal_list= p.map(cal_pentagonal, num_range)
p.close()
p.join()
print(pentagonal_list)

min_result = 99999

for i in range(len(pentagonal_list)-20):
    for j in range(i+1, i+20):
        if pentagonal_list[i] + pentagonal_list[j] in pentagonal_list:
            if pentagonal_list[j] - pentagonal_list[i] in pentagonal_list:
                print(pentagonal_list[j] - pentagonal_list[i])
