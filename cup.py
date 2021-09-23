class Cup:
    __height = 0
    __volume = 0
    __color = ''
    __material = ''

    def setHeight(self, height):
        try:
            height = int(height)
        except ValueError:
            print("请检查输入，要输入数字哦")
        else:
            if height > 0:
                self.__height = height
            else:
                print("请检查输入，必须为正数")

    def getHeight(self):
        return self.__height

    def setVolume(self, volume):
        try:
            volume = int(volume)
        except ValueError:
            print("请检查输入，要输入数字哦")
        else:
            if volume > 0:
                self.__volume = volume
            else:
                print("请检查输入，必须为正数")

    def getVolume(self):
        return self.__volume

    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

    def setMaterial(self, material):
        self.__material = material

    def getMaterial(self):
        return self.__material

    def save(self):
        print("这个{}的{}杯子，可以存放{}升液体".format(self.__color, self.__material, self.__volume))


c = Cup()
c.setHeight('a')
c.setHeight(-3)
c.setHeight(10)
c.setVolume(5)
c.setColor('red')
c.setMaterial('glass')
c.save()
print("这个杯子高{}cm".format(c.getHeight()))
