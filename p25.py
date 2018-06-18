import math

k0 = 1
k1 = 1

def gen_fibonacci_num(s0, s1):
    t = s1
    s1 = t + s0
    s0 = t
    return s0, s1

if __name__ == '__main__':
    for i in range(9999):
        k0, k1 = gen_fibonacci_num(k0, k1)
        print(str(i+3)+':'+ str(k1) + ':' + str(len(str(k1))))
        if len(str(k1)) > 1000:
            break
