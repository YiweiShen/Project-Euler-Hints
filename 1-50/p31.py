def check_coin(n):
    sum = 0
    for i in range(0, 201):
        for j in range(0, int((n-i)/2+1)):
            for k in range(0, int((n-i-2*j)/5+1)):
                for m in range(0, int((n-i-2*j-5*k)/10+1)):
                    for c in range(0, int((n-i-2*j-5*k-10*m)/20+1)):
                        for a in range(0, int((n-i-2*j-5*k-10*m-20*c)/50+1)):
                            for b in range(0, 3):
                                print('1p:'+str(i))
                                print('2p:'+str(j))
                                print('5p:'+str(k))
                                print('10p:'+str(m))
                                print('20p:'+str(c))
                                print('50p:'+str(a))
                                print('100p:'+str(b))
                                print(i+2*j+5*k+10*m+20*c+50*a+100*b)
                                if i+2*j+5*k+10*m+20*c+50*a+100*b == n:
                                    sum += 1
    return sum


if __name__ == '__main__':
    x = check_coin(200)
    print(x+1) # plus 2 pound alone
