from multiprocessing.pool import Pool

def is_palindromic(num):
    return str(num) == ''.join(reversed(str(num)))


def cal_lychrel(num):
    print(num)
    i = 0
    while i<55:
        s = num + int(''.join(reversed(str(num))))
        if is_palindromic(s):
            return None
        num = s
        i += 1
    return num

p = Pool(processes=16)
num_range = range(1, 10**4)
result_list = p.map(cal_lychrel, num_range)
p.close()
p.join()

result_list_clear = [x for x in result_list if x is not None]
print(len(result_list_clear))
