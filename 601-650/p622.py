
def cal_time(LEN):
    origenal = [x for x in range(LEN)]
    a = [x for x in range(LEN)]
    t = 1

    while True:
        a1 = a[:int(LEN/2)]
        a2 = a[int(LEN/2):]

        a = []
        for i in range(int(LEN/2)):
            a += [a1[i]]
            a += [a2[i]]
        if a == origenal:
            break
        else:
            t += 1

    return t

sum = 0

for i in range(144,145,2):
    test_time = cal_time(i)
    print(str(i)+':'+str(test_time))
    if test_time == 60:
        sum += i
        print('sum::::::::::'+str(sum))

print(sum)

