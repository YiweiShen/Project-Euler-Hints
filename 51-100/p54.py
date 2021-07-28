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


def compare_single_nums(num_str1, num_str2):
    while len(num_str1) > 0 and len(num_str2) > 0:
        if cal_highest_card(num_str1) > cal_highest_card(num_str2):
            return True
        if cal_highest_card(num_str1) < cal_highest_card(num_str2):
            return False
        num_str1.replace(cal_highest_card(num_str1),'')
        num_str2.replace(cal_highest_card(num_str2),'')
    return False


def cal_highest_card(num_str):
# High Card: Highest value card.
    highest_card = 0
    t = cal_card_number_value(num_str)
    for i in t:
        if i > highest_card:
            highest_card = i
    return highest_card


def cal_card_number_value(num_str):
    t = []
    for i in num_str:
        if i == 'T':
            t.append(10)
            continue
        if i == 'J':
            t.append(11)
            continue
        if i == 'Q':
            t.append(12)
            continue
        if i == 'K':
            t.append(13)
            continue
        if i == 'A':
            t.append(14)
            continue
        t.append(int(i))
    return t


def cal_num_value(num_str):
    sum = 0
    for i in num_str:
        sum += num_str.count(i)
    return sum


def is_flush(suit_str):
# Flush: All cards of the same suit.
    if suit_str.count(suit_str[0]) == 5:
        return suit_str[0]
    else:
        return False


def is_one_pair(num_str):
# One Pair: Two cards of the same value.
    if cal_num_value(num_str) == 7:
        for i in num_str:
            if num_str.count(i) == 2:
                return i
    else:
        return False


def is_two_pairs(num_str):
# Two Pairs: Two different pairs.
    if cal_num_value(num_str) == 9:
        some_str = []
        for i in num_str:
            if num_str.count(i) == 2 and i not in some_str:
                some_str.append(i)
        return some_str
    else:
        return False


def is_three_of_a_kind(num_str):
# Three of a Kind: Three cards of the same value.
    if cal_num_value(num_str) == 11:
        for i in num_str:
            if num_str.count(i) == 3:
                return i
    else:
        return False


def is_straight(num_str):
# Straight: All cards are consecutive values.
    if cal_num_value(num_str) == 5:
        t = cal_card_number_value(num_str)
        test = []
        for i in t:
            for j in t:
                if i - j > 4:
                    return False
        return True
    else:
        return False


def is_full_house(num_str):
# Full House: Three of a kind and a pair.
    return cal_num_value(num_str) == 13


def is_four_of_a_kind(num_str):
# Four of a Kind: Four cards of the same value.
    if cal_num_value(num_str) == 17:
        for i in num_str:
            if num_str.count(i) == 4:
                return i
    else:
        return False


def is_straight_flush(num_str, suit_str):
# Straight Flush: All cards are consecutive values of same suit.
    return is_straight(num_str) and is_flush(suit_str)


def is_royal_flush(num_str, suit_str):
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
    return cal_highest_card(num_str) == 14 and is_straight_flush(num_str, suit_str)


for i in range(1000):
    print('in the hand of: '+ p1[i] + ', highest card is '+str(cal_highest_card(p1_value_list[i])), end=',')
    if is_one_pair(p1_value_list[i]):
        print(' one pair of: '+ str(is_one_pair(p1_value_list[i])), end=',')
    if is_two_pairs(p1_value_list[i]):
        print(' two pairs: '+ str(is_two_pairs(p1_value_list[i])[0])+' and '+ str(is_two_pairs(p1_value_list[i])[1]), end=',')
    if is_three_of_a_kind(p1_value_list[i]):
        print(' three of a kind: '+ str(is_three_of_a_kind(p1_value_list[i])), end=',')
    if is_straight(p1_value_list[i]):
        print(' it is straight', end=',')
    if is_flush(p1_suit_list[i]):
        print(' flush', end=',')
    if is_full_house(p1_value_list[i]):
        print(' full house', end=',')
    if is_four_of_a_kind(p1_value_list[i]):
        print(' four of a kind: '+ str(is_four_of_a_kind(p1_value_list[i])), end=',')
    if is_straight_flush(p1_value_list[i], p1_suit_list[i]):
        print(' straight flush', end=',')
    if is_royal_flush(p1_value_list[i], p1_suit_list[i]):
        print(' royal flush', end=',')
    print('')





