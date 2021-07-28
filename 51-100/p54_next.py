with open('p054_poker.txt') as f:
    c = f.readlines()

p1 = []
p2 = []
p1_value_list = ['' for i in range(1000)]
p1_suit_list = ['' for i in range(1000)]
p2_value_list = ['' for i in range(1000)]
p2_suit_list = ['' for i in range(1000)]

for i in range(len(c)):
    p1.append(c[i][:14])
    p2.append(c[i][15:-1])

for j in range(len(c)):
    for i in range(0, 14, 3):
        p1_value_list[j] += str(p1[j][i])
        p2_value_list[j] += str(p2[j][i])

    for i in range(1, 14, 3):
        p1_suit_list[j] += str(p1[j][i])
        p2_suit_list[j] += str(p2[j][i])


def cal_highest_card(num_str):
# High Card: Highest value card.
    highest_card = 0
    t = cal_card_number_value(num_str)
    for i in t:
        if i > highest_card:
            highest_card = i
    return highest_card


def re_cal_card_value(some_value):
    if some_value == 'T':
        return 10
    if some_value == 'J':
        return 11
    if some_value == 'Q':
        return 12
    if some_value == 'K':
        return 13
    if some_value == 'A':
        return 14
    return int(some_value)


def cal_card_number_value(num_str):
    t = []
    for i in num_str:
        t.append(int(re_cal_card_value(i)))
    return t


def cal_num_value(num_str):
    sum = 0
    for i in num_str:
        sum += num_str.count(i)
    return sum


def is_flush(suit_str):
# Flush: All cards of the same suit.
    if suit_str.count(suit_str[0]) == 5:
        return 10**19
    else:
        return 0


def is_one_pair(num_str):
# One Pair: Two cards of the same value.
    if cal_num_value(num_str) == 7:
        for i in num_str:
            if num_str.count(i) == 2:
                return re_cal_card_value(i)*10**10
    else:
        return 0


def is_two_pairs(num_str):
# Two Pairs: Two different pairs.
    if cal_num_value(num_str) == 9:
        some_str = []
        for i in num_str:
            if num_str.count(i) == 2 and i not in some_str:
                some_str.append(i)
        a = re_cal_card_value(some_str[0])
        b = re_cal_card_value(some_str[1])
        if a > b:
            return a*10**14 + b*10**12
        else:
            return b*10**14 + a*10**12
    else:
        return 0


def is_three_of_a_kind(num_str):
# Three of a Kind: Three cards of the same value.
    if cal_num_value(num_str) == 11:
        for i in num_str:
            if num_str.count(i) == 3:
                return re_cal_card_value(i)*10**16
    else:
        return 0


def is_straight(num_str):
# Straight: All cards are consecutive values.
    if cal_num_value(num_str) == 5:
        t = cal_card_number_value(num_str)
        test = []
        for i in t:
            for j in t:
                if i - j > 4:
                    return 0
        return 10**18
    else:
        return 0


def is_full_house(num_str):
# Full House: Three of a kind and a pair.
    if cal_num_value(num_str) == 13:
        t = 0
        for i in num_str:
            if num_str.count(i) == 3:
                t += re_cal_card_value(i)*10**22
        for i in num_str:
            if num_str.count(i) == 2:
                t += re_cal_card_value(i)*10**20
        return t
    else:
        return 0

def is_four_of_a_kind(num_str):
# Four of a Kind: Four cards of the same value.
    if cal_num_value(num_str) == 17:
        for i in num_str:
            if num_str.count(i) == 4:
                return re_cal_card_value(i)*10**24
    else:
        return False


def is_straight_flush(num_str, suit_str):
# Straight Flush: All cards are consecutive values of same suit.
    if is_straight(num_str) and is_flush(suit_str):
        return 10**26
    else:
        return 0


def cal_num_sorted_list(num_str):
    num_list = []
    for i in num_str:
        num_list.append(re_cal_card_value(i))
    sum = 0
    t = 1
    for i in sorted(num_list):
        sum += i * t
        t *= 100
    return sum

# def is_royal_flush(num_str, suit_str):
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
#    return cal_highest_card(num_str) == 14 and is_straight_flush(num_str, suit_str)

p1_whole_num = []
p2_whole_num = []

for i in range(0, 1000):
    p1_whole_num.append(is_straight_flush(p1_value_list[i], p1_suit_list[i]) + is_four_of_a_kind(p1_value_list[i]) + is_full_house(p1_value_list[i]) + is_flush(p1_suit_list[i]) + is_straight(p1_value_list[i]) + is_three_of_a_kind(p1_value_list[i]) + is_two_pairs(p1_value_list[i]) + is_one_pair(p1_value_list[i]) + cal_num_sorted_list(p1_value_list[i]))
    p2_whole_num.append(is_straight_flush(p2_value_list[i], p2_suit_list[i]) + is_four_of_a_kind(p2_value_list[i]) + is_full_house(p2_value_list[i]) + is_flush(p2_suit_list[i]) + is_straight(p2_value_list[i]) + is_three_of_a_kind(p2_value_list[i]) + is_two_pairs(p2_value_list[i]) + is_one_pair(p2_value_list[i]) + cal_num_sorted_list(p2_value_list[i]))

result_sum = 0
result_list =[]
for i in range(0, 1000):
    if p1_whole_num[i] > p2_whole_num[i]:
        result_list.append(i)
        result_sum += 1

print(result_list)
print(result_sum)
# print(p1[256])
# print(p2[256])

'''
8S JS 6D 4H JH
6H 6S 6C KS KH
'''
# for i in range(1000):
#     print('----------------')
#     print(p1[i])
#     print(p1_whole_num[i])
#     print(p2[i])
#     print(p2_whole_num[i])

# correct player 1 wining hands are
# [1, 2, 5, 6, 9, 11, 12, 17, 19, 21, 26, 28, 29, 30, 31, 32, 34, 37, 39, 42, 43, 47, 49, 52, 56, 60, 64, 65, 66, 68, 70, 71, 75, 78, 79, 82, 84, 85, 86, 87, 90, 95, 100, 105, 109, 111, 112, 120, 121, 122, 126, 127, 129, 134, 135, 137, 139, 144, 146, 147, 149, 157, 160, 163, 166, 167, 171, 173, 174, 175, 176, 182, 188, 189, 190, 196, 198, 200, 203, 204, 211, 213, 218, 222, 229, 232, 234, 235, 236, 240, 241, 243, 246, 247, 249, 251, 254, 264, 266, 270, 271, 273, 278, 279, 280, 285, 286, 288, 289, 290, 292, 296, 304, 307, 309, 311, 314, 318, 320, 321, 322, 323, 326, 329, 332, 335, 338, 344, 347, 348, 353, 357, 359, 360, 364, 366, 367, 368, 374, 377, 380, 381, 383, 393, 397, 401, 403, 410, 411, 412, 414, 418, 422, 423, 425, 431, 432, 434, 436, 439, 441, 447, 448, 453, 454, 458, 459, 465, 466, 468, 469, 472, 474, 477, 479, 484, 488, 489, 491, 493, 494, 496, 497, 498, 499, 500, 503, 505, 511, 524, 525, 527, 528, 533, 537, 540, 549, 552, 555, 557, 559, 560, 562, 563, 564, 565, 567, 568, 569, 570, 575, 578, 584, 589, 590, 597, 598, 601, 602, 603, 604, 608, 610, 623, 624, 632, 633, 639, 640, 641, 645, 649, 652, 655, 657, 658, 659, 662, 663, 667, 670, 671, 675, 676, 679, 681, 682, 683, 685, 689, 690, 691, 692, 695, 696, 697, 700, 701, 702, 703, 704, 705, 706, 708, 711, 717, 718, 719, 721, 724, 725, 731, 733, 736, 742, 744, 747, 749, 753, 757, 760, 761, 763, 771, 772, 773, 774, 775, 778, 784, 785, 786, 790, 793, 796, 798, 802, 803, 807, 809, 811, 813, 814, 818, 819, 821, 826, 829, 830, 833, 834, 835, 838, 839, 840, 843, 844, 848, 854, 856, 859, 862, 867, 868, 870, 871, 875, 883, 884, 885, 886, 887, 889, 891, 896, 904, 906, 907, 912, 914, 916, 918, 920, 922, 928, 930, 931, 932, 933, 938, 939, 940, 946, 947, 949, 950, 953, 954, 957, 959, 961, 965, 971, 972, 973, 975, 977, 980, 982, 983, 986, 988, 989, 992, 998, 999]
