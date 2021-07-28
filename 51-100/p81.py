with open('p081_matrix.txt') as f:
    content = f.readlines()

print(content)

clear_list = []

for i in range(0, len(content)):
    clear_list.append(content[i].strip().split(','))

for i in range(1,80):
    clear_list[0][i] = int(clear_list[0][i]) + int(clear_list[0][i-1])

for i in range(1,80):
    clear_list[i][0] = int(clear_list[i][0]) + int(clear_list[i-1][0])

for i in range(1, 80):
    for j in range(1, 80):
        if int(clear_list[i-1][j]) < int(clear_list[i][j-1]):
            clear_list[i][j] = int(clear_list[i][j]) + int(clear_list[i-1][j])
            continue
        clear_list[i][j] = int(clear_list[i][j]) + int(clear_list[i][j-1])

print(clear_list[79][79])
