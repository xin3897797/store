lst = []
print("请输入一串数字，以q结束:")
while True:
    num = input()
    if num == 'q':
        break
    else:
        if num.isdigit():
            lst.append(int(num))
        else:
            print("请输入数字")
count = {}
for l in lst:
    if l not in count.keys():
        count[l] = 1
    else:
        count[l] = count[l] + 1
print(count)
