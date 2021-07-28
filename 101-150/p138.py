import time
from multiprocessing.pool import Pool
from decimal import Decimal


start_time = time.time()


def check(num):
    print(num)
    num = Decimal(num)
    a = (num*num + ((num-1)/2)**2)**Decimal(0.5)
    b = (num*num + ((num+1)/2)**2)**Decimal(0.5)
    if a == Decimal(int(a)):
        return int(a)
    if b == Decimal(int(b)):
        return int(b)
    return None

p = Pool(processes=16)
num_range = range(3, 10**7)
result_list = p.map(check, num_range)
p.close()
p.join()

result_list_clear = [x for x in result_list if x is not None]

print(result_list_clear)

# after finding the first five L numbers, I googled the sequences, and found it is
# A007805 - OEIS
# https://oeis.org/A007805
# so answer would be:
# [17, 305, 5473, 98209, 1762289, 31622993, 567451585, 10182505537, 182717648081, 3278735159921, 58834515230497, 1055742538989025]
# the speed will be very very slow if I try to find the answer by brute force
