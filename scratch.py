import pandas

# 读取Excel表
data = pandas.read_excel("C:\\Users\\lenovo\\Desktop\\12月份衣服销售数据.xls")

# 获取数据
date = list(data['日期'])
cloth = list(data['服装名称'])
money = list(data['价格/件'])
number = list(data['库存数量'])
sale = list(data["销售量/每日"])

print("------------------12月衣服销售数量----------------")
print("日期", " "*3, "服装名称", " "*4, "价格/件", " "*3, "库存数量", " "*3, "销售量/每日")
for i in range(30):
    print(date[i], "\t", cloth[i], "\t\t", money[i], "\t\t", number[i], "\t\t", sale[i])

print("总销售额：", sum(sale))
print("平均每日销售数量：", round(sum(sale)/len(date), 1))

cloth_dict = {}
for i in range(30):
    if cloth[i] not in cloth_dict.keys():
        cloth_dict[cloth[i]] = sale[i]
    else:
        cloth_dict[cloth[i]] = cloth_dict[cloth[i]] + sale[i]
print("-------每个种类月销售量占比-----")
print("种类", " "*2, "月销售量", " "*2, "占比")

for i in cloth_dict.keys():
    per = (cloth_dict[i]/sum(sale))*100
    print(i, "\t", cloth_dict[i], "\t", str(round(per, 2))+'%')
