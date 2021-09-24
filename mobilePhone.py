class OldPhone:
    __brand = ''

    def setBrand(self, brand):
        self.__brand = brand

    def getBrand(self):
        return self.__brand

    def call(self, name):
        print(f"正在给{name}打电话...")


class NewPhone(OldPhone):
    def call(self, name):
        print("语音拨号中...")
        super().call(name)

    def phoneIntro(self):
        print(f"品牌为：{self.getBrand()}的手机很好用...")


n = NewPhone()
n.setBrand('vivo')
n.phoneIntro()
n.call('lily')
