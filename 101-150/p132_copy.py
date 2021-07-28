import math

######## Sieve of Erastosthenes part #########
MAX = 200000
isprime = [False,False]

#fill with Trues
for i in range(2,MAX+1):
    isprime.append(True)

#begin sieving
j = 2
for j in range(2,MAX+1):
    if isprime[j] == True:
        k = j
        for k in range (2*k,MAX+1,k):
            isprime[k] = False
##### End of Sieve of Erastosthenes part #####

factornum = 0
factorsum = 0
i = 7
while (factornum<40):
    if isprime[i] and pow(10,10**9,i)==1:
        factorsum+=i
        factornum+=1
    i+=1
print(factorsum)
