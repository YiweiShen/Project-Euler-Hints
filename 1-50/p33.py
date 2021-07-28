if __name__ == '__main__':
    for i in range(1,10):
        for j in range(i+1,10):
            for m in range(1, 10):
                if i/j == (10*i+m)/(10*m+j) or i/j == (10*j+m)/(10*m+i):
                    print(i, j)
                    print(10*i+m, 10*m+j,10*j+m, 10*m+i)
