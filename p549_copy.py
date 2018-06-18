import time

def total_similar_factors(number, divisor):
    count = 0

    while number % divisor == 0:
        number /= divisor
        count  += 1

    return int(count)

def result(n):
    final_list = [0] * (n + 1)

    for i in range(2, n + 1):
        if final_list[i] == 0:
            highest_value = 0
            multiplier    = i
            skip_number   = 0

            while multiplier <= n:
                if skip_number == 0:
                    highest_value += i
                    skip_number   += total_similar_factors(highest_value, i)

                iteration = multiplier

                while iteration <= n:
                    if highest_value > final_list[iteration]:
                        final_list[iteration] = highest_value

                    iteration += multiplier

                skip_number -= 1
                multiplier  *= i

    return sum(final_list)

start_time = time.time()

print(result(10 ** 6))
print("{} ms".format(round(1000 * (time.time() - start_time))))
