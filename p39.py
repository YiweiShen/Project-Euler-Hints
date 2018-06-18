def is_solution(a_num,b_num,c_num):
    return a_num**2 + b_num**2 == c_num**2


if __name__ == '__main__':
    for p in range(1000, 1, -1):
        sum = 0
        print('p:'+str(p))
        for a in range(1, int(p/3+1)):
            for b in range(1, int(2*p/3-a+1)):
                if b < a:
                    continue
                c = p-a-b
                if c < b:
                    continue
                if is_solution(a, b, c):
                    sum += 1
        print(sum)

