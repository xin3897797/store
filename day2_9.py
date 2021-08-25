# 99乘法表倒序打印
i = 1
j = 9
while j >= 1:
    while i <= j:
        print("{}*{}={}".format(i, j, i*j), end='\t')
        i = i + 1
    print()
    j = j - 1
    i = 1