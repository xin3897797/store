import random
import pymysql

uid_list = []
account_bank = '中国工商银行的昌平支行'
menu = '''
        ****************************************
        *     中国工商银行                       *"
        *     账户管理系统                       *"
        *        V1.0                          *"
        "***************************************"
        "                                       "
        *1.开户                                 *"
        *2.存钱                                 *"
        *3.取钱                                 *"
        *4.转账                                 *"
        *5.查询                                 *"
        *6.Bye!                                *"
        ****************************************"
'''
info = '''
        -------------用户信息--------------------
        账号：{}
        用户名：{}
        密码：******
        国家：{}
        省份：{}
        街道：{}
        门牌号：{}
        余额：{}
        开户行：{}
'''


# 提前创建数据库和表
def connect_mysql():
    conn = pymysql.connect(
        host='127.0.0.1',
        port=3306,
        db='bank',
        user='root',
        passwd='root',
        charset='utf8mb4'
    )
    cursor = conn.cursor()
    return cursor, conn


def get_uid(cur):
    cur.execute(
        """select uid from user_info"""
    )
    data = cur.fetchall()
    for d in data:
        uid_list.append(d[0])


def close_mysql(cur, conn):
    cur.close()
    conn.close()


def add_user(t_dict):
    cur, conn = connect_mysql()
    get_uid(cur)
    if t_dict['uid'] in uid_list:
        return 2
    else:
        if len(uid_list) == 100:
            return 3
        else:
            cur.execute(
                """insert into user_info(uid,name,password,country,province,street,door,deposit,account_bank)
                value(%s,%s,%s,%s,%s,%s,%s,%s,%s)""",
                (t_dict['uid'], t_dict['name'], t_dict['password'], t_dict['country'], t_dict['province'],
                 t_dict['street'], t_dict['door'], t_dict['deposit'], account_bank)
            )
            conn.commit()
            close_mysql(cur, conn)
            return 1


def save_money(uid, money):
    cur, conn = connect_mysql()
    get_uid(cur)
    cur.execute(
        """select deposit from user_info where uid=%s""",
        uid
    )
    deposit = cur.fetchone()
    money += deposit[0]
    if uid in uid_list:
        cur.execute(
            """update user_info set deposit=%s where uid=%s""",
            (deposit[0] + money, uid)
        )
        conn.commit()
        close_mysql(cur, conn)
        return True
    else:
        return False


def withdraw_money(uid, password, money):
    cur, conn = connect_mysql()
    get_uid(cur)
    cur.execute(
        """select password,deposit from user_info where uid=%s""",
        uid
    )
    data = cur.fetchone()
    if uid in uid_list:
        if password == data[0]:
            if money <= data[1]:
                cur.execute(
                    """update user_info set deposit=%s where uid=%s""",
                    (data[1] - money, uid)
                )
                conn.commit()
                close_mysql(cur, conn)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


def transfer(out_id, in_id, out_passwd, money):
    cur, conn = connect_mysql()
    get_uid(cur)
    cur.execute(
        """select password,deposit from user_info where uid=%s""",
        out_id
    )
    out_data = cur.fetchone()
    cur.execute(
        """select deposit from user_info where uid=%s""",
        in_id
    )
    in_data = cur.fetchone()
    if out_id and in_id in uid_list:
        if out_passwd == out_data[0]:
            if money <= out_data[1]:
                cur.execute(
                    """update user_info set deposit=%s where uid=%s""",
                    (out_data[1] - money, out_id)
                )
                cur.execute(
                    """update user_info set deposit=%s where uid=%s""",
                    (in_data[0] + money, in_id)
                )
                conn.commit()
                close_mysql(cur, conn)
                return 0
            else:
                return 3
        else:
            return 2
    else:
        return 1


def user_info(uid, passwd):
    cur, conn = connect_mysql()
    get_uid(cur)
    cur.execute(
        """select * from user_info where uid=%s""",
        uid
    )
    data = cur.fetchone()
    if uid in uid_list:
        if passwd == data[2]:
            print(info.format(data[0], data[1], data[3], data[4], data[5], data[6], data[7], data[8]))
        else:
            print("密码错误")
    else:
        print("该用户不存在")


if __name__ == '__main__':
    print(menu)
    while True:
        sel = int(input("请输入业务编号："))
        if sel == 1:
            uid = str(random.randint(0, 99999999)).zfill(8)  # zfill(8)的作用就是当字符串不够8位时，在首位填充0
            name = input("请输入用户姓名：")
            password = input("请输入用户密码(6位数字)：")
            print("请输入用户地址：")
            country = input("\t\t请输入国家：")
            province = input("\t\t请输入省份：")
            street = input("\t\t请输入街道：")
            door = input("\t\t请输入门牌号：")
            temp = {'uid': uid, 'name': name, 'password': password, 'country': country, 'province': province,
                    'street': street, 'door': door, 'deposit': 0}
            result = add_user(temp)
            if result == 1:
                print("用户添加成功，用户信息如下")
                print(info.format(uid, name, country, province, street, door, 0, account_bank))
            elif result == 2:
                print("用户账号已存在，请重新操作")
            elif result == 3:
                print("用户库注册已满，无法添加新用户")
        elif sel == 2:
            account = input("请输入用户账号：")
            money = float(input("请输入存入金额："))
            re = save_money(account, money)
            if re:
                print("存入成功")
            else:
                print("没有此用户，请检查用户账号")
        elif sel == 3:
            acc = input("请输入用户账号：")
            passwd = input("请输入用户密码：")
            withdraw = float(input("请输入取钱金额："))
            r = withdraw_money(acc, passwd, withdraw)
            if r == 1:
                print("用户不存在，请检查用户账号")
            elif r == 2:
                print("密码错误，请检查用户密码")
            elif r == 3:
                print("存款不足，请检查取出金额")
            else:
                print("取出成功")
        elif sel == 4:
            out_account = input("请输入转出账号：")
            in_account = input("请输入转入账号：")
            out_passwd = input("请输入转出账号密码：")
            money = float(input("请输入转出金额："))
            res = transfer(out_account, in_account, out_passwd, money)
            if res == 1:
                print("用户不存在，请检查转入和转出账号")
            elif res == 2:
                print("密码不正确，请检查转出账号密码")
            elif res == 3:
                print("存款不足，请检查转出金额")
            else:
                print("转账成功")
        elif sel == 5:
            user_id = input("请输入用户账号：")
            user_passwd = input("请输入用户密码：")
            user_info(user_id, user_passwd)
        elif sel == 6:
            print("退出系统中……")
            break
        else:
            print("输入错误，请检查编号")
