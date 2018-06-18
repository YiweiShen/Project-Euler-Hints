def cal_square_num(num):
    sum = 0
    for i in range(1, int(num/4)+2):
        print(i)
        if i % 2 == 0:
            for j in range(2, int(num/4)+2, 2):
                if 0 < i*i-j*j <= num:
                    sum += 1
                else:
                    continue
        else:
            for j in range(1, int(num/4)+2, 2):
                if 0 < i*i-j*j <= num:
                    sum += 1
                else:
                    continue
    return sum


if __name__ == '__main__':
    print(cal_square_num(10**6))
