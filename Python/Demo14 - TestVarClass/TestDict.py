
# 初始化字典
normaldict = {}

# 赋值
normaldict["1"] = "zzr"

normaldict["2"] = {
    "3": "freya"
}

# 带变量的赋值

for x in range(5, 7):
    normaldict[x] = {
        "4": "monika",
        "999": "monika1"
    }

if __name__ == '__main__':
    print(normaldict)

