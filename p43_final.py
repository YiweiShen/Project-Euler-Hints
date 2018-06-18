import math
from multiprocessing.pool import Pool


def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)



def find_at_idx(idx):
    print(idx)
    digits = [0,1,2,3,4,5,6,7,8,9]
    answer = []
    numdigits = 10
    while len(digits) != 1:
        a = fact(numdigits-1)
        b = int(math.ceil(idx/float(a)))
        thisdigit = digits[b-1]
        answer.append(thisdigit)
        digits.remove(thisdigit)
        idx = idx - (a*(b-1))
        numdigits = numdigits - 1
    else:
        answer.append(digits[0])
    return ''.join([str(x) for x in answer])



num_range = range(1, fact(10)+1)
p=Pool(processes=16)
pandigital_list = p.map(find_at_idx, num_range)
p.close()
p.join()
print(pandigital_list)

result_list =[]
for i in pandigital_list:
    print(i)
    if int(i[1:4]) % 2 == 0 and int(i[2:5]) % 3 == 0 and int(i[3:6]) % 5 == 0 and int(i[4:7]) % 7 == 0 and int(i[5:8]) % 11 == 0 and int(i[6:9]) % 13 == 0 and int(i[7:10]) % 17 == 0:
        result_list.append(i)

sum = 0
print(result_list)
for i in result_list:
    sum += int(i)

print(sum)
