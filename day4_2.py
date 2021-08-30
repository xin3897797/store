fruits = {
    "苹果": 12.3,
    "草莓": 4.5,
    "香蕉": 6.3,
    "葡萄": 5.8,
    "橘子": 6.4,
    "樱桃": 15.8
}

info = {
    '小明': {
        'fruits': {'苹果': 4, '草莓': 13, '香蕉': 10},
        'money': 0
    },
    '小刚': {
        'fruits': {'葡萄': 19, '橘子': 12, '樱桃': 30},
        'money': 0
    }
}


def money(f, i):
    moneys = 0
    for key in i['fruits'].keys():
        moneys += f[key] * i['fruits'][key]
    i['money'] = moneys


name = input("请输入要计算的人名：")
money(fruits, info[name])
print(info[name])
