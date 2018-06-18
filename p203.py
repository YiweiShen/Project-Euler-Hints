
from multiprocessing.pool import Pool
import time

t = time.time()
LINE_NUM = 51
matrix = [[0 for x in range(LINE_NUM)] for y in range(LINE_NUM)]

matrix[0][0] = 1

for i in range(1, LINE_NUM):
    matrix[i][0] = 1
    matrix[i][i] = 1

print(matrix)

def is_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return None
    return num

for i in range(2, LINE_NUM):
    for j in range(1, i):
        matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]

print(matrix)

list_num = []

for i in range(0, LINE_NUM):
    for j in range(0, LINE_NUM):
        list_num.append(matrix[i][j])

list_num_clear = list(set([x for x in list_num if x is not 0]))
print(list_num_clear)
print(max(list_num_clear))

p=Pool(processes=16)
num_range = range(2, 11243248)

prime_list = p.map(is_prime, num_range)
p.close()
p.join()
prime_list_clear = [x for x in prime_list if x is not None]
print(prime_list_clear)

def is_squarefree(num):
    print(num)
    for i in prime_list_clear:
        if i*i > list_num_clear[num]:
            return list_num_clear[num]
        if list_num_clear[num] % (i*i) == 0:
            return None



p=Pool(processes=16)
num2_range = range(0, len(list_num_clear))
result_list = p.map(is_squarefree, num2_range)
p.close()
p.join()
result_list_clear = [x for x in result_list if x is not None]
print(sum(result_list_clear))
print('time:'+str(time.time()-t))
