import time

t =time.time()
NUM_LIMIT = 10**6


def cal_primes(limit):
    nums_log = [True] * (limit+1)
    nums_value = []
    for i in range(limit+1):
        nums_value += [i]
    nums_log[0] = nums_log[1] = False

    for (i, is_prime) in enumerate(nums_log):
        if is_prime:
            nums_value[i] -= 1
            for n in range(i + i, limit + 1, i):
                nums_log[n] = False
                nums_value[n] -= nums_value[n] // i
    return nums_value


values = cal_primes(NUM_LIMIT)
print(values)
result = sum(values[2:])
print(result)

print('time:'+str(time.time()-t))
