from multiprocessing.pool import Pool

ts_list =[]

for i in range(1, 10001):
    print(i)
    k = i
    j = k**2
    k +=1
    j += k**2
    while j < 10**8:
        ts_list.append(j)
        k += 1
        j += k**2

def is_palindromic(num):
    check = ts_list[num]
    print(check)
    if str(check) == str(check)[::-1]:
        return check
    return None

print(ts_list)


p = Pool(processes=100)
num_range = range(0, len(ts_list))
result_list = p.map(is_palindromic, num_range)
p.close()
p.join()
result_list_clear = [x for x in result_list if x is not None]
print(result_list_clear)
result_list_clear = list(set(result_list_clear))
print(result_list_clear)
print(sum(result_list_clear))


