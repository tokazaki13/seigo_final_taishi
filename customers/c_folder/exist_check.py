#入力内容がリスト・辞書に存在するか確認

def exist_check(input,list):
    if input not in list:
        return False
    else:
        return True


"""a = exist_check(2,[1,2,3])
print(a)

b = exist_check(2,[1,3])
print(b)
"""
