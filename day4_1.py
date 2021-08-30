dict = {"k1": "v1", "k2": "v2", "k3": "v3"}
for key in dict.keys():
    print(key, end='')
print()
for value in dict.values():
    print(value, end='')
print()
dict["k4"] = "v4"
print(dict)
