# 判断能否形成三角形，什么三角形
import math
a, b, c = int(input()), int(input()), int(input())
if a+b > c > abs(a - b):
    print("能形成三角形")
    if a == b != c or b == c != a or a == c != b:
        print("是等腰三角形")
    elif a == b == c:
        print("是等边三角形")
    elif math.sqrt(a*a+b*b) == c or math.sqrt(c*c+b*b) == a or math.sqrt(a*a+c*c) == b:
        print("是直角三角形")
    else:
        print("是普通三角形")
else:
    print("不能形成三角形")
