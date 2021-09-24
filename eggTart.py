"""
蛋挞篮子：500个蛋挞
三个厨师，同时做蛋挞，每做一个放入到篮子中。如果篮子满了，等待3秒。
六个用户，每个人手里有3000元，每个蛋挞2元。当篮子蛋挞不够时，等待2秒钟，一直到钱花光为止。
"""

from threading import Thread
import time

basket = 0  # 蛋挞篮子
money = 3000
state = 0  # 用于判断是否6个用户全部没钱了
count = 0  # 用于记录用户买了多少个蛋挞


class Chef(Thread):
    name = ''

    def run(self) -> None:
        global basket
        global state
        while True:
            if state == 6:
                print(f"用户都没钱了，{self.name}停止生产蛋挞")
                break
            else:
                if basket == 500:
                    print("篮子满了，等待3秒钟")
                    time.sleep(3)
                else:
                    basket += 1
                    print(f"{self.name}做了一个蛋挞")


class User(Thread):
    name = ''

    def run(self) -> None:
        global basket
        global money
        global state
        global count
        while True:
            if money == 0:
                state += 1
                print(f"您的资金不足，此次您购买了{count}个蛋挞")
                break
            else:
                if basket == 0:
                    print("蛋挞不够了，请等待2秒")
                    time.sleep(2)
                else:
                    money -= 2
                    basket -= 1
                    count += 1
                    print(f"{self.name}买了一个蛋挞")


c1 = Chef()
c2 = Chef()
c3 = Chef()
u1 = User()
u2 = User()
u3 = User()
u4 = User()
u5 = User()
u6 = User()

c1.name = 'c1'
c2.name = 'c2'
c3.name = 'c3'
u1.name = 'u1'
u2.name = 'u2'
u3.name = 'u3'
u4.name = 'u4'
u5.name = 'u5'
u6.name = 'u6'

c1.start()
c2.start()
c3.start()
u1.start()
u2.start()
u3.start()
u4.start()
u5.start()
u6.start()
