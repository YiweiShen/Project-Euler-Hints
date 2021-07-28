import itertools

with open('p098_words.txt') as f:
    c = f.readlines()


word_list = c[0].replace('"','').split(',')


def is_anagram(a,b):
    return sorted(list(a)) == sorted(list(b))

word_pairs =[]
for i in range(0, len(word_list)):
    for j in range(i+1, len(word_list)):
        if is_anagram(word_list[i],word_list[j]):
            word_pairs.append((word_list[i], word_list[j]))

print(word_pairs)


def sq(n):
    x = int(''.join(y[letter_set[i]] for i in n))
    return x if int(x**0.5)**2 == x else False

max_sq = 0

for w, a in word_pairs:
    letter_set = {x:y for y, x in enumerate(set(w))}
    for y in itertools.permutations('123456789', len(letter_set)):
        if sq(w) and sq(a): max_sq = max(sq(w), sq(a), max_sq)


print(max_sq)

# NUM = 6
# try_list = []

# for i in range(int(10**(NUM-1)**0.5), int((10**NUM)**0.5)):
#     if len(str(i*i)) == NUM:
#         try_list.append(i*i)

# print(try_list)

# def change_num(a):
#     k = list(str(a))
#     b = k[0] + k[1] + k[4] + k[3] + k[2] + k[5]
#     return int(b)


# result_list =[]

# for i in try_list:
#     if change_num(i) in try_list:
#         result_list.append(i)

# if len(result_list) > 0:
#     print(result_list)
# else:
#     print('no answer')
