# 一只青蛙掉在井里了，井高20米，青蛙白天网上爬3米，晚上下滑2米，问第几天能出来
high = 20
daytime = 3
night = 2
day = 1
while True:
    if 3*day-2*day >= 20:
        print(day)
        break
    else:
        day += 1

