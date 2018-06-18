

def primes_sieve(limit):
    a = [True] * limit                          # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            continue
        else:
            for n in range(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
    return a

a = primes_sieve(100)

print(a[87])
