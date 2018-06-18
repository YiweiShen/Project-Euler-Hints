target = 100
ns = range(1, target)
ways = [1] + [0]*target

for n in ns:
    for i in range(n, target+1):
        ways[i] += ways[i-n]

print(ways[100])


# https://blog.dreamshire.com/project-euler-76-solution/
