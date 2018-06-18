from time import time


NUM_LIMIT = 10**2
start_time = time()

the_list = [1,2,1]
result = 0

def conv(num,b):
    convStr = "0123456789abcdefghijklmnopqrstuvwxyz"
    if num<b:
        return convStr[num]
    else:
        return conv(num//b,b) + convStr[num%b]


for i in range(NUM_LIMIT-3):
    copy_the_list = [1]
    for j in range(1,len(the_list)):
        copy_the_list.append((the_list[j-1]+the_list[j])%7)
    result += copy_the_list.count(0)
    print(str(conv(i+4, 7))+':'+str(len(copy_the_list)+1-copy_the_list.count(0)))
    the_list = copy_the_list+[1]





result = (1+NUM_LIMIT)*NUM_LIMIT/2 - result
print(result)

print('time:'+str(time()-start_time))

