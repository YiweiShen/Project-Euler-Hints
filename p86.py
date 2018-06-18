import time
from multiprocessing.pool import Pool



if __name__ == '__main__':
    start = time.time()

    def try_check(LIMIT):
        sum = 0
        # for a in range(1, LIMIT):
        #     for b in range(1, LIMIT):
        #         z = 2*a*a + b*b
        #         t = (z + 2*min(a*b, a*a))**0.5
        #         if t == int(t):
        #             sum += 1
# always sqrt of (a+b)^2 + c*2 will be shortest if 1<=a<=b<=c<=LIMIT

        for ab in range(2, 2*LIMIT+1):
            for c in range(int(ab/2)+1, LIMIT+1):
                t = (c*c + ab*ab)**0.5
                if t == int(t):
                    for a in range(1, ab):
                        b = ab - a
                        if a<=b<=c:
                            sum +=1
        return sum

    #for i in range(100, 10000,100):
    # 17s find i between 1800 and 1900
    for i in range(1800, 1900):
        t = try_check(i)
        print(str(i)+':'+str(t))
        if t > 1000000:
            break

    print('time:'+str(time.time()-start))

# 17s + 43s = 60s find 1818
