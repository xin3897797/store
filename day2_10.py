# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来
high = 20
daytime = 3
night = 2
day = 0
hig = 0
while True:
    if hig >= high:
        print(day)
        break
    else:
        day += 1
        hig += 3
        if hig >= high:
            print(day)
            break
        else:
            hig -= 2



