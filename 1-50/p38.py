from multiprocessing.pool import Pool

def try_pandigital(num):
    print(num)
    sum_num = num
    i = 1
    while int(sum_num)<10**10 and len(set(str(sum_num))) == len(str(sum_num)) and '0' not in str(sum_num):
        i += 1
        sum_num = int(str(sum_num)+str(num * i))
    return str(sum_num)[:-len(str(num * i))]

p = Pool(processes=16)
num_range = range(1,10**6)
result_list = p.map(try_pandigital, num_range)
p.close()
p.join()
print(result_list)
max_num = 0
for i in result_list:
    if i is not '' and int(i)>max_num:
        max_num = int(i)

print(max_num)
