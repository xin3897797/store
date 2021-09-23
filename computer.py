class Computer:
    __screen_size = ''
    __price = 0
    __cpu = ''
    __memory_size = ''
    __standby_time = ''

    def setScreenSize(self, screen_size):
        self.__screen_size = screen_size

    def getScreenSize(self):
        return self.__screen_size

    def setPrice(self, price):
        try:
            price = float(price)
        except ValueError:
            print("请输入数字")
        else:
            if price > 0:
                self.__price = price
            else:
                print("请输入正数")

    def getPrice(self):
        return self.__price

    def setCpu(self, cpu):
        self.__cpu = cpu

    def getCpu(self):
        return self.__cpu

    def setMemorySize(self, memory_size):
        self.__memory_size = memory_size

    def getMemorySize(self):
        return self.__memory_size

    def setStandbyTime(self, standby_time):
        self.__standby_time = standby_time

    def getStandbyTime(self):
        return self.__standby_time

    def typing(self):
        print("正在打字中……，请注意待机时长为{}".format(self.__standby_time))

    def game(self):
        print("正在打游戏中……，内存大小为{}".format(self.__memory_size))

    def watching(self):
        print("正在看视频中，屏幕大小为{}".format(self.__screen_size))


c = Computer()
c.setScreenSize('12寸')
c.setPrice('a')
c.setPrice(-2000)
c.setPrice(3000)
c.setCpu('Inter Core i5-7200U')
c.setMemorySize('8G')
c.setStandbyTime('1小时05分钟')
print("现在有一台笔记本电脑，设备信息如下")
print("屏幕大小：{}\n价格：{}\nCPU型号：{}\n内存大小：{}\n待机时长：{}".format(c.getScreenSize(), c.getPrice(), c.getCpu(),
                                                          c.getMemorySize(), c.getStandbyTime()))
while True:
    select = input("请选择要进行的行为：打字、打游戏、看视频，如果不想做请按任意键退出:")
    if select == '打字':
        c.typing()
    elif select == '打游戏':
        c.game()
    elif select == '看视频':
        c.watching()
    else:
        break



