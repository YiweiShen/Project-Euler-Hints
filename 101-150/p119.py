k_list = []

for i in range(1, 1000):
    for j in range(1,10):
        if sum(int(i) for i in list(str(i**j))) == i:
            if len(str(i**j))>1:
                k_list.append(i**j)

print(k_list)
print(sorted(k_list)[1])
print(sorted(k_list)[9])
print(sorted(k_list)[29])
print(len(k_list))
