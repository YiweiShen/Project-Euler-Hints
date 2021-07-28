LIMIT = 10**6
import math


def cal_item(num):
    if num < int(LIMIT**0.5)+1:
        return math.ceil(num/2)-1
    else:
        x = math.ceil((num*num-LIMIT)**0.5)
        if num % 2 == 0:
            if x % 2 == 0:
                return (num-x)/2
            else:
                return (num-x-1)/2
        else:
            if x % 2 == 0:
                return (num-x-1)/2
            else:
                return (num-x)/2

sum = 0
for i in range(1, int(LIMIT/4)+2):
    print('i:'+str(i))
    print(cal_item(i))
    sum += cal_item(i)

print(int(sum))
