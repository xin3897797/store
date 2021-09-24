class Chef:
    __name = ''
    __age = 0

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setAge(self, age):
        try:
            age = int(age)
        except ValueError:
            print("请检查输入，要输入数字哦")
        else:
            if age > 0:
                self.__age = age
            else:
                print("请检查输入，必须为正数")

    def getAge(self):
        return self.__age

    def steaming(self):
        print("蒸饭方法：...")


class ChefA(Chef):
    def cooking(self):
        print("炒菜方法：...")


class ChefB(ChefA):
    def steaming(self):
        print("蒸饭")

    def cooking(self):
        print("炒菜")


b = ChefB()
b.setName("张三")
b.setAge(30)
print(f"厨师姓名为{b.getName()}，今年{b.getAge()}岁")
b.steaming()
b.cooking()
