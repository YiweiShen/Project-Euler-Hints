dic_cal = {}


def cal(a, b):
    if (a, b) in dic_cal:
        return dic_cal[(a, b)]
    return cal(a - 1, b) + cal(a, b - 1)


if __name__ == '__main__':
    for j in range(0, 1):
        for k in range(0, 21):
            dic_cal[(j, k)] = 1
    for j in range(0, 21):
        for k in range(0, 1):
            dic_cal[(j, k)] = 1
    for j in range(0, 21):
        for k in range(0, 21):
            dic_cal[(j, k)] = cal(j, k)
    print(cal(20, 20))
