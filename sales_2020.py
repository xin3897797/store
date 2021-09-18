import xlrd

wb = xlrd.open_workbook(filename=r"C:\Users\lenovo\Desktop\2020年每个月的销售情况.xlsx")
# 全年的销售总额
sales_sum = []
sumx = 0
for s in range(0, 12):
    sheet = wb.sheet_by_index(s)
    price = sheet.col_values(2)
    sales_volume = sheet.col_values(4)
    for i in range(1, len(price)):
        sumx += round(price[i] * sales_volume[i], 1)
    sales_sum.append(round(sumx, 1))
    sumx = 0
print("全年的销售总额：", round(sum(sales_sum), 1))
print("--------------------------------------------------")

# 每件衣服的销售（件数）占比
cloth_sales_volume = {}
cloth_sum = 0
for s in range(0, 12):
    sheet = wb.sheet_by_index(s)
    for i in range(1, sheet.nrows):
        row_value = sheet.row_values(i)
        cloth_sum += row_value[4]
        if row_value[1] not in cloth_sales_volume.keys():
            cloth_sales_volume[row_value[1]] = row_value[4]
        else:
            cloth_sales_volume[row_value[1]] += row_value[4]
print("每件衣服的销售（件数）占比如下：")
for c in cloth_sales_volume.keys():
    print("{}:{}%".format(c, round((cloth_sales_volume[c] / cloth_sum) * 100, 2)))
print("--------------------------------------------------")

# 每件衣服的月销售占比
sales_month = []
cloth_month_sales = {}
for s in range(0, 12):
    sheet = wb.sheet_by_index(s)
    sales_volume = sheet.col_values(4)
    del sales_volume[0]
    sales_month.append(round(sum(sales_volume), 1))
    for i in range(1, sheet.nrows):
        row_value = sheet.row_values(i)
        if row_value[1] not in cloth_month_sales.keys():
            cloth_month_sales[row_value[1]] = {s: row_value[4]}
        else:
            temp_dict = cloth_month_sales[row_value[1]]
            if s in temp_dict.keys():
                temp_dict[s] += row_value[4]
            else:
                temp_dict[s] = row_value[4]
            cloth_month_sales[row_value[1]] = temp_dict

print("每件衣服的月销售占比：")
for cloth in cloth_month_sales.keys():
    print("{}".format(cloth))
    for month, sale in cloth_month_sales[cloth].items():
        print("\t{}月销售占比为：{}%".format(month + 1, round((sale / sales_month[month]) * 100, 2)))
print("--------------------------------------------------")

# 每件衣服的销售额占比
cloth_sale = {}
for s in range(0, 12):
    sheet = wb.sheet_by_index(s)
    for r in range(1, sheet.nrows):
        row_value = sheet.row_values(r)
        if row_value[1] in cloth_sale.keys():
            cloth_sale[row_value[1]] += row_value[2] * row_value[4]
        else:
            cloth_sale[row_value[1]] = row_value[2] * row_value[4]
print("每件衣服的销售额占比:")
for cloth in cloth_sale.keys():
    print("{}的销售额占比为：{}%".format(cloth, round(cloth_sale[cloth] / sum(sales_sum) * 100, 2)))
print("--------------------------------------------------")

# 销量最高和最低
c = sorted(cloth_sales_volume.items(), key=lambda x: x[1])
print("最畅销的衣服是：{}".format(c[-1][0]))
print("全年销量最低的衣服是：{}".format(c[0][0]))
print("--------------------------------------------------")


# 每个季度最畅销的衣服
def quarter_sale(temp, row):
    if row[1] in temp.keys():
        temp[row[1]] += row[4]
    else:
        temp[row[1]] = row[4]
    return temp


cloth_quarter = {'第一季度': {}, '第二季度': {}, '第三季度': {}, '第四季度': {}}
for s in range(0, 12):
    sheet = wb.sheet_by_index(s)
    for r in range(1, sheet.nrows):
        row_value = sheet.row_values(r)
        if s in [1, 2, 3]:
            temp_dict = cloth_quarter['第一季度']
            cloth_quarter['第一季度'] = quarter_sale(temp_dict, row_value)
        elif s in [4, 5, 6]:
            temp_dict = cloth_quarter['第二季度']
            cloth_quarter['第二季度'] = quarter_sale(temp_dict, row_value)
        elif s in [7, 8, 9]:
            temp_dict = cloth_quarter['第三季度']
            cloth_quarter['第三季度'] = quarter_sale(temp_dict, row_value)
        elif s in [10, 11, 0]:
            temp_dict = cloth_quarter['第四季度']
            cloth_quarter['第四季度'] = quarter_sale(temp_dict, row_value)
for q in cloth_quarter.keys():
    c = sorted(cloth_quarter[q].items(), key=lambda x: x[1])
    print("{}最畅销的衣服是：{}".format(q, c[-1][0]))
print("--------------------------------------------------")
