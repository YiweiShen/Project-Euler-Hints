import fractions


def cal_e_list():
    e_list = []
    for i in range(1, 35):
        e_list.append(1)
        e_list.append(2*i)
        e_list.append(1)
    return e_list

def cal_seq(seq_num, some_list):
    temp_list = []
    for i in some_list[:seq_num-1]:
        temp_list.append(i)
    c1 = 1
    c2 = 0
    print(temp_list)
    for i in reversed(temp_list):
        print(i)
        c1, c2 = i * c1 + c2, c1
        print('c1:'+str(c1))
        print('c2:'+str(c2))
    return c2+2*c1


def cal_helper(b,c):
    return b*c+1


if __name__ == '__main__':
    the_elist = cal_e_list()
    print(the_elist)
    a = cal_seq(100, the_elist)
    print(a)
    print(sum([int(x) for x in list(str(a))]))

