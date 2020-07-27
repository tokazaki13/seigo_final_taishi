#半角チェック
def check_half(keyword):
    import get_bite_count

    count = len(keyword)
    bite = get_bite_count.get_east_asian_width_count(keyword)
    if count == bite:
        return True
    else:
        print("全角文字が入力されています\n半角で入力してください")
        return False

def check_count(keyword,limit,min):

    count = len(keyword)
    if min <= count <= limit:
        return True
    elif count > limit:
        print("文字数制限を超過しています")
        print(str(limit) + "字以内で入力して下さい")
        return False
    else:
        print("最低文字数を下回っています")
        print(str(min) + "字以上で入力して下さい")
        return False

"""a = ["あ","あいうえおかきく","。＊＋‘＠＾－”"]
for test in a:
    c = check_count(test,8,1)
    print(c)"""

"""a = ["","あいうえおかきくけ","abcdefghi"]
for test in a:
    c = check_count(test,8,1)
    print(c)"""

"""a = ["a","A"," "]
for test in a:
    c = check_half(test)
    print(c)"""

"""a = ["　","あいうえおかきくけ","abcえーびーし"]
for test in a:
    c = check_half(test)
    print(c)"""

"""
郵便番号の時
if min == limit:
    以内、以上を消す
"""
