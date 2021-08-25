# 输入10个数字，打印最大的数、和、平均数
list_ten1 = []
for i in range(10):
    a = int(input("输入第{}个数字：".format(i+1)))
    list_ten1.append(a)
print("最大值：", max(list_ten1))
print("求和：", sum(list_ten1))
print("平均数：", sum(list_ten1)/len(list_ten1))