#二つのリストを〇〇：△△に変換し表示する
def list_for_read(list,input_data):
    for list_name, data in zip(list,input_data):
        if type(data) is int:
            data = str(data)
        print(list_name + "：" + data)


def list_to_dict(list,input_data):
    my_dict = dict(zip(list,input_data))
    return my_dict

"""list_for_read(["名前","電話番号","メールアドレス","郵便番号","住所","配送地域ID"],[1,1,1,1,1,2])
"""
