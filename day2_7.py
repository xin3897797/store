# 打印图形
tamp = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
lst = []
dic = {}
for i in range(1, 8):
    if i == 1:
        dic[i] = [7]
    else:
        temp = []
        for x in dic[i-1]:
            temp.append(x-1)
            temp.append(x+1)
        dic[i] = sorted(list(set(temp)))
for h in dic.keys():
    for j in dic[h]:
        tamp[j-1] = '*'
    lst.append(''.join(tamp))
for k in lst:
    print(k)
