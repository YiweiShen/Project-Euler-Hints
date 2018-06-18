import itertools


def check(list1, list2):
    check_sum = True
    for i in list1:
        check_sum = check_sum and (list2.index(int(i[:1])) < list2.index(int(i[-1:])))
    return check_sum


if __name__ == '__main__':
    key_list = []
    with open('p079_keylog.txt') as f:
        key_list = f.readlines()
    for i in range(len(key_list)):
        key_list[i] = key_list[i].strip()
    key_set = []
    for i in range(len(key_list)):
        first_part = key_list[i][:2]
        last_part = key_list[i][-2:]
        key_set.append(first_part)
        key_set.append(last_part)
    key_set = list(set(key_set))
    print(key_set)
    num_appeared = []
    for i in range(0,10):
        for j in key_set:
            if str(i) in j:
                num_appeared.append(i)

    num_appeared = list(set(num_appeared))
    print(num_appeared)

    iter_list = list(itertools.permutations(num_appeared,len(num_appeared)))
    for i in iter_list:
        if check(key_set, list(i)):
            print(i)
