from multiprocessing.pool import Pool

def cal_right_triangle_num(num):
    print(num)
    sum = 0
    for a in range(1, int(num/3)):
        for b in range(int(num/3), int(num/2)):
            c = num - a - b
            if a < c < b:
                if a*a + c*c == b*b:
                    sum += 1
                    if sum == 2:
                        return 2
            else:
                continue
    return sum


p = Pool(processes=16)
num_range = range(1, 15000)
result_list = p.map(cal_right_triangle_num, num_range)
p.close()
p.join()

print(result_list.count(1))
