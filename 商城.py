import random


shop = [
    ["联想电脑", 4500],
    ["Mac Pc", 12000],
    ["HUA WEI WATCH", 1200],
    ["海尔洗衣机", 5000],
    ["卫龙辣条", 3.5],
    ["老干妈", 15],
    ["乌江榨菜", 1.5]
]
mycart = []
choose = ''

money = int(input("请初始化您的余额："))

while True:
    for key, value in enumerate(shop):
        print(key, value)
    # 领优惠券
    discount = random.randint(0, 39)
    if discount in range(0, 10):
        choose = input("恭喜你获得一张5折联想电脑优惠券，请问您是否使用？(y/n)")
        if choose == 'y':
            if money < (shop[0][1]*0.5):
                print("对不起，您的余额不够，不能进行本次购买")
            else:
                mycart.append([shop[0][0], shop[0][1]*0.5])
                money -= shop[0][1]*0.5
                print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
    elif discount in range(10, 30):
        choose = input("恭喜你获得一张6折老干妈优惠券，请问您是否使用？(y/n)")
        if choose == 'y':
            if money < (shop[5][1]*0.6):
                print("对不起，您的余额不够，不能进行本次购买")
            else:
                mycart.append([shop[5][0], shop[5][1]*0.6])
                money = money - (shop[5][1]*0.6)
                print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
    elif discount in range(30, 40):
        choose = input("恭喜你获得一张9折乌江榨菜优惠券，请问您是否使用？(y/n)")
        if choose == 'y':
            if money < (shop[6][1]*0.9):
                print("对不起，您的余额不够，不能进行本次购买")
            else:
                mycart.append([shop[6][0], shop[6][1]*0.9])
                money = money - (shop[6][1]*0.9)
                print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
    if choose == 'n':
        chose = input("亲输入您要的商品编号：")
        if chose.isdigit():
            chose = int(chose)
            #  这个商品是否存在
            if chose > len(shop):  # len(shop) = 7
                print("该商品不存在！请重新输入：")
            else:
                # 看钱够不够
                if money < shop[chose][1]:
                    print("对不起，您的余额不够，不能进行本次购买")
                else:
                    mycart.append(shop[chose])
                    money = money - shop[chose][1]
                    print("恭喜，添加购物车成功！您的余额还剩：", money, "!")
        elif chose == 'q' or chose == 'Q':
            print("欢迎下次光临！")
            break
        else:
            print("输入非法!请重新输入：")

# 结算,打印购物小条
print("以下是您的购物小条，请查收：")
print("----------------------------")
for key, value in enumerate(mycart):
    print(key, value)
print("您本次余额还剩：￥", money)
print("----------------------------")
