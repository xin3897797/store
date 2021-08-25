# while循环 99乘法表
i = 1
j = 1
while i <= 9:
    while j <= i:
        print("{}*{}={}".format(i, j, i*j), end='\t')
        j = j + 1
    print()
    i = i + 1
    j = 1