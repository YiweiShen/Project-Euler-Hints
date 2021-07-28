import itertools

the_str = '1234567'*5
rainbow_list = list(itertools.permutations(the_str, 20))

len_of_rainbow = len(rainbow_list)

sum_of_rainbow = 0

for i in rainbow_list:
    sum_of_rainbow += len(set(i))

print(sum_of_rainbow/len_of_rainbow)
