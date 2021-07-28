name_score = 0


def cal_name_score(n, list_a):
    global name_score
    name_s = 0
    for i in list_a[n]:
        name_s += ord(i.lower()) - 96
    name_score += name_s * (n+1)
    return name_score


if __name__ == '__main__':
    with open('p022_names.txt') as f:
        name_list = f.readlines()
    clear_list = name_list[0].replace('"', '').split(',')
    sorted_list = sorted(clear_list)
    for i in range(0, len(sorted_list)):
        cal_name_score(i, sorted_list)
    print(name_score)
