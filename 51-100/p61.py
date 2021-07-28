def cal_triangle(n):
    return int(n*(n+1)/2)

def cal_square(n):
    return n * n

def cal_pentagonal(n):
    return int(n*(3*n - 1)/2)


def cal_hexagonal(n):
    return n*(2*n-1)

def cal_heptagonal(n):
    return int(n*(5*n-3)/2)

def cal_octagonal(n):
    return n*(3*n-2)


lists = [[] for i in range(6)]

for i in range(1,1000):
    if cal_triangle(i)< 1000:
        continue
    if cal_triangle(i)> 10000:
        break
    lists[0].append(cal_triangle(i))

for i in range(1,1000):
    if cal_square(i)< 1000:
        continue
    if cal_square(i)> 10000:
        break
    lists[1].append(cal_square(i))

for i in range(1,1000):
    if cal_pentagonal(i)< 1000:
        continue
    if cal_pentagonal(i)> 10000:
        break
    lists[2].append(cal_pentagonal(i))

for i in range(1,1000):
    if cal_hexagonal(i)< 1000:
        continue
    if cal_hexagonal(i)> 10000:
        break
    lists[3].append(cal_hexagonal(i))

for i in range(1,1000):
    if cal_heptagonal(i)< 1000:
        continue
    if cal_heptagonal(i)> 10000:
        break
    lists[4].append(cal_heptagonal(i))

for i in range(1,1000):
    if cal_octagonal(i)< 1000:
        continue
    if cal_octagonal(i)> 10000:
        break
    lists[5].append(cal_octagonal(i))

all_list = []
for i in range(6):
    print(lists[i])
    all_list += lists[i]

def find_next(a, blist):
    clist = []
    for i in blist:
        if str(a)[2:] == str(i)[:2]:
            clist.append(i)
    return clist


