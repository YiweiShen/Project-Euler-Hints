import math

if __name__ == '__main__':
    with open('p099_base_exp.txt') as f:
        content = f.readlines()

    print(content)
    l = []
    for i in range(0, 1000):
        l.append(content[i].replace('\n','').split(','))
    l2 = []
    for i in range(0, 1000):
        x = math.log2(int(l[i][0]))*int(l[i][1])
        l2.append(x)
    max = 0
    for i in range(0, 1000):
        if l2[i]>max:
            max = l2[i]
            print(i+1)    # for line number
    print('done')
