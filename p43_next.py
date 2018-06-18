l17 = []
l13 = []
l11 = []
l7 = []
l5 = []
l3 = []
l2 = []

i = 0
while i * 17 < 1000:
    l17.append(i*17)
    i += 1

i = 0
while i * 13 < 1000:
    l13.append(i*13)
    i += 1

i = 0
while i * 11 < 1000:
    l11.append(i*11)
    i += 1

i = 0
while i * 7 < 1000:
    l7.append(i*7)
    i += 1

i = 0
while i * 5 < 1000:
    l5.append(i*5)
    i += 1

i = 0
while i * 3 < 1000:
    l3.append(i*3)
    i += 1

i = 0
while i * 2 < 1000:
    l2.append(i*2)
    i += 1

for i in range(0, len(l17)):
    for j in range(0, len(l13)):
        if str(l17[i]).zfill(3)[0:2] == str(l13[j]).zfill(3)[1:3]:
            print(l17[i])
            print(l13[j])
