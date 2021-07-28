from time import time
start_time = time()
count = [0 for k in range(250)]
t = [0 for k in range(250)]

for i in range(1,250251):
    count[pow(i, i, 250)] += 1

t[0] = 1
for i in range(250):
    for j in range(count[i]):
        t = [(t[k] + t[(k-i)]) % 10**16 for k in range(250)]

print(t[0]-1)
print('time'+str(time()-start_time))
