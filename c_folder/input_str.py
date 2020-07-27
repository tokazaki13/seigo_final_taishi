def input_str():
    import EC_exit
    while True:
        try:
            str = input()
        except KeyboardInterrupt:
            print("CTRL+Cが入力されました。")
            EC_exit.EC_exit()
        return str
"""a = input_str()
print(a)"""
