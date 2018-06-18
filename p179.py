import math

def cal_divisor_num(num):
    sum = 0
    for a in range(1, int(math.sqrt(num)) + 1):
        if num % a == 0:
            sum += 1
    if int(math.sqrt(num)) == math.sqrt(num):
        return sum * 2 - 1
    return sum * 2


l = []
sum = 0

if __name__ == '__main__':
    for i in range(1,10**7):
        print(i)
        l.append(cal_divisor_num(i))
    print(l)
    for j in range(0,len(l)-1):
        if l[j] == l[j+1]:
            sum += 1
    print(sum)

# this script can produce the right answer, however, too slow
