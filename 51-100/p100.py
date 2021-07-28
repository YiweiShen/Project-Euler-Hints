from multiprocessing.pool import Pool


def check(num):
    a = int(num*(num-1)/2)
    b = int(a ** 0.5)
    if b*(b+1) == a:
        print(b)


p=Pool(processes=16)
num_range = range(10**12, int(10**12*1.1))
p.map(check, num_range)
p.close()
p.join()
