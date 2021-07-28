from multiprocessing.pool import Pool

def calcNum(n):#some arbitrary, time-consuming calculation on a number
    print("Calcs Started on "+str(n))
    m = n
    for i in range(5000000):
        m += i % 25
        if m > n*n:
            m /= 2
    return int(m)

if __name__ == "__main__":
    p = Pool(processes=10)

    nums = range(50)
    finList = []


    result = p.map(calcNum, nums)
    p.close()
    p.join()

    print(result)
