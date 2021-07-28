from time import time


NUM_LIMIT = 50000000  # changed for 146
start_time = time()
result_list = [0 for i in range(NUM_LIMIT)]

for u in range(1, NUM_LIMIT+1):
    print(u)
    v = 1
    while u*v<NUM_LIMIT:
        if 3*v>u and (u+v)%4 ==0  and (3*v-u)%4 ==0:
            result_list[u*v] += 1
        v += 1

result = 0
for i in range(NUM_LIMIT):
    if result_list[i] == 1:  # changed for 136
        result += 1

print(result)

print('time:'+str(time()-start_time))
