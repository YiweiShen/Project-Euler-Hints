import time

t =time.time()


def find_primes(limit):
    nums = [True] * (limit + 1)
    nums[0] = nums[1] = False

    for (i, is_prime) in enumerate(nums):
        if is_prime:
            for n in range(i * i, limit + 1, i):
                nums[n] = False
    return nums

primes = find_primes(10**8+1)


def is_prime(num):
    for i in range(2, int(num**0.5+1)):
        if num % i == 0:
            return False
    return True


def check(num):
    print(num)
    for i in range(2, int(num**0.5+1)):
        if num % i == 0 and not is_prime(i+num/i):
            return False
    return num

sum_result = 0

for (i, it_is_prime) in enumerate(primes):
    if it_is_prime:
        if check(i-1):
            sum_result += i-1


print(sum_result)

print('time:'+str(time.time()-t))
