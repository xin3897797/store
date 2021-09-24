class Person:
    __age = 0
    __gender = ''
    __name = ''

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

    def setGender(self, gender):
        self.__gender = gender

    def getGender(self):
        return self.__gender

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name


class Worker(Person):
    def work(self):
        print(f"{self.getName()}正在干活中……")


class Student(Person):
    __student_id = ''

    def setStudentId(self, sid):
        self.__student_id = sid

    def getStudentId(self):
        return self.__student_id

    def study(self):
        print(f"{self.getName()}正在学习中……")

    def sing(self):
        print(f"{self.getName()}正在唱歌中……")


s = Student()
s.setName("李华")
s.setAge(21)
s.setGender("男")
s.setStudentId("123456")
s.sing()
s.study()

w = Worker()
w.setName("张三")
w.setAge(30)
w.setGender('男')
w.work()
