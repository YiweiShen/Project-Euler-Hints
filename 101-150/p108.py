def cal_time(n):
    k = n*n
    s=0
    for i in range(1, n+1):
        if k % i == 0:
            s+=1
    print(str(n)+':'+str(s))
    return s

a = 2

while cal_time(a)<1000:
    a +=1


prime_list = [2,3,5,7,11,13,17]
