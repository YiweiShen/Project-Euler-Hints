def spiral(num):
    p = 1
    sum = 1
    for i in range(1, int((num-1)/2)+1):
        for j in range(1, 5):
            k = 2 * i
            p += k
            print('sum:'+str(sum))
            sum += p
    return sum


if __name__ == '__main__':
    print(spiral(1001))
