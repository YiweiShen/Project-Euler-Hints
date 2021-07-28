def test(some_str):
    x1,y1,x2,y2,x3,y3 = int(some_str.split(',')[0]),int(some_str.split(',')[1]),int(some_str.split(',')[2]),int(some_str.split(',')[3]),int(some_str.split(',')[4]),int(some_str.split(',')[5])
    k1 = x1*(y1-y2)+y1*(x2-x1)
    k2 = x2*(y2-y3)+y2*(x3-x2)
    k3 = x3*(y3-y1)+y3*(x1-x3)
    if k1>0 and k2>0 and k3>0:
        return 1
    if k1<0 and k2<0 and k3<0:
        return 1
    return 0

with open('p102_triangles.txt') as f:
    c = f.readlines()

k =[]
for i in c:
    k.append(test(i))

print(sum(k))
