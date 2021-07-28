from multiprocessing.pool import Pool

def check(num):
    sq = num * num
    if str(sq)[0]=='1' and str(sq)[2]=='2' and str(sq)[4]=='3' and str(sq)[6]=='4' and str(sq)[8]=='5' and str(sq)[10]=='6' and str(sq)[12]=='7' and str(sq)[14]=='8' and str(sq)[16]=='9' and str(sq)[18]=='0':
        print('###############################')
        print(num)
        print(num*num)
        print('###############################')


if __name__ == '__main__':
    num_range = range(1376696080, 1389026623, 10)
    p = Pool(processes=100)
    p.map(check, num_range)
    p.close()
    p.join()
