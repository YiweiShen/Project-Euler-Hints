def digital_sum(num):
    sum = 0
    for i in list(str(num)):
        sum += int(i)
    return sum


if __name__ == '__main__':
    sum_max = 0
    for a in range(99,1,-1):
        for b in range(99,1,-1):
            x = digital_sum(a**b)
            if x > sum_max:
                sum_max = x
                print(x)
