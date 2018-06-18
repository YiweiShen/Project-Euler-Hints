from multiprocessing.pool import Pool

def cal_prime_factors(n):
    factors=[]
    d=2
    while(d*d<=n):
        while(n>1):
            while n%d==0:
                factors.append(d)
                n=n/d
            d+=1
    return len(set(factors))


def check(n):
    if cal_prime_factors(n) == 4 and cal_prime_factors(n+1) == 4 and cal_prime_factors(n+2) == 4 and cal_prime_factors(n+3) == 4:
        # this method is very slow, and a lot of repeat calculations
        print(n)
        return n
    return None

if __name__ == '__main__':
    p = Pool(processes=16)
    num_range =range(10**5,10**6)
    p.map(check,num_range)
    p.close()
    p.join()
