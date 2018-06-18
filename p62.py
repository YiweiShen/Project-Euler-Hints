cubes = {}
n = 1
min_cube = float('Inf')
d = ''

while min_cube == float('Inf'):
    c = n*n*n
    d = ''.join(sorted(str(c)))
    if d in cubes:
        cubes[d] += [c]
        if len(cubes[d]) == 5:
            min_cube = cubes[d][0]
    else:
        cubes[d] = [c]
    n += 1

print(min_cube)
