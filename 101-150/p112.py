def is_bouncy(n):
    n_list = list(str(n))
    k=[]
    for i in range(1, len(n_list)):
        k.append(int(n_list[i-1])-int(n_list[i]))
    flag = 0
    for i in k:
        if i < 0:
            flag += 1
            break
    for i in k:
        if i > 0:
            flag += 1
            break
    if flag == 2:
        return True
    return False


k = 0
for i in range(100,10**7):
    if is_bouncy(i):
        k += 1
        print(str(i)+':'+str(k/i))
        if k/i > 0.99:
            break
