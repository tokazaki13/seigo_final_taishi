#動作表示関数
#dict{1:"はい",2:"いいえ"}のようなものが入る
def options(dict):
    for a,b in dict.items():
        print(str(a) + "：" + b)


"""test = {1:"はい",2:"いいえ"}

options(test)"""
