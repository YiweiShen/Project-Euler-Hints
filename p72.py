def HCF(x, y):
   while(y):
       x, y = y, x % y
   return x

d = 10**4
sum = 0
for i in range(1, d+1):
    print(i)
    for j in range(i+1, d+1):
        if HCF(i,j)==1:
            sum += 1

print(sum)
