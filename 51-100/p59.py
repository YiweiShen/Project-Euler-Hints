with open('p059_cipher.txt') as f:
    c = f.readlines()

r = c[0].split(',')

sum = 0
for t in range(len(r)):
    if t % 3 == 0:
        print(chr(int(r[t]) ^ ord('g')), end ='')
        sum += int(r[t]) ^ ord('g')
        continue
    if t % 3 == 1:
        print(chr(int(r[t]) ^ ord('o')), end ='')
        sum += int(r[t]) ^ ord('o')
        continue
    else:
        print(chr(int(r[t]) ^ ord('d')), end ='')
        sum += int(r[t]) ^ ord('d')

print(sum)
