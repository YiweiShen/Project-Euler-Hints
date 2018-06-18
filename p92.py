dic = {}

def cal_chain(num):
    num_original = num
    while True:
        if num in dic.keys():
            return dic[num]
        l = list(str(num))
        sum = 0
        for i in l:
            sum += int(i)**2
        if sum == 1 or sum == 89:
            dic[num_original]=sum
            return sum
        num = sum

def cal_chain_next(num):
    while True:
        if num in dic.keys():
            return dic[num]
        l = list(str(num))
        sum = 0
        for i in l:
            sum += int(i)**2
        if sum == 1 or sum == 89:
            return sum
        num = sum


for i in range(1,500):
    cal_chain(i)

result = 0
for i in range(1, 10**7):
    print(i)
    if cal_chain_next(i) == 89:
        result += 1

print(result)
