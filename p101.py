# https://blog.dreamshire.com/project-euler-101-solution/
# the idea comes from the web page
# no idea why it is

def U(n):
    return 1-n+n*n-n**3+n**4-n**5+n**6-n**7+n**8-n**9+n**10


def cal_diff_list(some_list):
    result_list = []
    for i in range(1, len(some_list)):
        result_list.append(some_list[i]-some_list[i-1])
    return result_list

u_list = []

for i in range(1, 11):
    u_list.append(U(i))

print(u_list)
sum_u = 0

while len(u_list)>0:
    sum_u += sum(u_list)
    u_list = cal_diff_list(u_list)

print(sum_u)
