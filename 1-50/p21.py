def cal_amicable_sum(n):
    sum = 0
    for i in range(1, int(n/2)+1):
        if n % i == 0:
            sum += i
    return sum

l = []

if __name__ == '__main__':
    a = 0
    for i in range(1, 10000):
        if i == cal_amicable_sum(cal_amicable_sum(i)) and i != cal_amicable_sum(i):
            print(str(i)+':'+str(cal_amicable_sum(i)))
            a += i
    print('a:'+str(a))
