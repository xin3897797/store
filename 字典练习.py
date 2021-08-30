region_dict = {
    "北京": {"昌平区": {"回龙观": "育荣教育园区"},
           "通州区": {"结研所": "北京胸科医院"},
           "海淀区": {"丹棱街": "中国电子大厦"}},
    "河北": {"邯郸市": {"邯山区": "青年大街"},
           "廊坊市": {"三河市": "海油大街"}}
}


def get_region(p):
    if p in region_dict.keys():
        c = input("请输入市/区：")
        if c in region_dict[p].keys():
            s = input("请输入街道/区：")
            if s in region_dict[p][c].keys():
                print(region_dict[p][c][s])
            else:
                print("请检查街道/区名称正确")
        else:
            print("请检查市/区名称正确")
    else:
        print("检查省份名称")


if __name__ == '__main__':
    while True:
        province = input("请输入一个省份：")
        if province == 'q':
            break
        else:
            get_region(province)
