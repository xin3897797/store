import xlrd
import pymysql
wb = xlrd.open_workbook(r"C:\Users\lenovo\Desktop\2020年每个月的销售情况.xlsx")
conn = pymysql.connect(host='localhost', port=3306, db='company', user='root', passwd='root')
cursor = conn.cursor()

for s in range(0, 12):
    sheet = wb.sheet_by_index(s)
    for r in range(1, sheet.nrows):
        row_value = sheet.row_values(r)
        sql = '''insert into sales value(%s,%s,%s,%s,%s,%s)'''
        param = [str(s+1)+'月', row_value[0], row_value[1], row_value[2], row_value[3], row_value[4]]
        cursor.execute(sql, param)
        conn.commit()
    print("{}月数据提交成功".format(s+1))
cursor.close()
conn.close()
