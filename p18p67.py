

if __name__ == '__main__':
    with open('p067_triangle.txt') as f:
        list_a = f.readlines()

    high = len(list_a)
    matrix = [[0 for x in range(high)] for y in range(high)]
    for i in range(0, high):
        for j in range(0, i+1):
            matrix[i][j] = int(list_a[i][3*j:3*j+2])
    print(matrix)

    for i in range(1, high):
        for j in range(0, i+1):
            if j == 0:
                matrix[i][j] += matrix[i-1][j]
                continue
            matrix[i][j] += max(matrix[i-1][j-1], matrix[i-1][j])
    print(max(matrix[high-1]))
