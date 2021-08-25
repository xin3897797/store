# 登录系统三次密码输入错误锁定功能，用户名：root，密码：admin
print("----------登录系统——————")
input("输入用户名：")
password = input("输入密码：")
if password == 'admin':
    print("登陆成功")
else:
    print("登录失败，密码错误")
    password1 = input("请再次输入密码：")
    if password1 == 'admin':
        print("登陆成功")
    else:
        print("登录失败，密码错误")
        password2 = input("请再次输入密码：")
        if password2 == 'admin':
            print("登陆成功")
        else:
            print("登录失败，系统锁定")