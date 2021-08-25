# 输入10个数字，且求和
list_ten = []
for i in range(10):
    a = int(input("输入第{}个数字:".format(i+1)))
    list_ten.append(a)
print("10个数字和为：", sum(list_ten))
