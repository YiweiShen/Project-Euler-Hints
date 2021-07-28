def check(num):
    sum = 0
    for i in list(str(num)):
        sum += int(i)**5
    return num == sum


if __name__ == '__main__':
    whole_sum = 0
    for i in range(1,999999):
        if check(i):
            whole_sum += i
    print(whole_sum-1)  # exclude 1^5
