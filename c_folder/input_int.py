#数値を入力させる。

def input_int():
    import EC_exit
    while True:
        try:
            num = int(input("数値を入力してください："))
        except ValueError:
            print("数字以外が入力されました。")
            continue
        except KeyboardInterrupt:
            print("CTRL+Cが入力されました。")
            EC_exit.EC_exit()
        return num
"""a = input_int()
print(a)"""
#全角半角数値OK
