# 20以内的阶乘
sum = 0
jc = 1
j = 1
for i in range(1, 21):
    while j <= i:
        jc = jc * j
        j = j + 1
    sum = sum + jc
print(sum)
