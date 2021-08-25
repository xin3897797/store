'''
猜字游戏
初始资金为100，每猜一次扣除10，资金为0或对才结束游戏
'''
import random
count = 0
money = 100
num = random.randint(0, 5)
while True:
    a = int(input("请输入一个0~4的数字"))
    count += 1
    if a == num:
        print("成功，数字为{}，共猜测{}次".format(a, count))
        break
    else:
        print("失败", a)
        money -= 10
        if money == 0 :
            print("锁定系统……")
            input("按回车退出系统")
            break
