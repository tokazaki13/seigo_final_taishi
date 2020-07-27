def yes_no():
    import options
    import input_int
    import exist_check

    print("------------------\n入力情報を確定してもよろしいですか：")
    transitions = {1:"はい",2:"いいえ"}

    options.options(transitions)
    print("★注意★\n「いいえ」を選択すると、前の画面に戻り、登録時は再度情報を入力していただく必要があります")
    num = input_int.input_int()
    while exist_check.exist_check(num,transitions) is False:
        print("適切な選択肢を選択してください")
        options.options(transitions)
        num = input_int.input_int()
    return num

"""a = yes_no()
print(a)"""

def yes_no_only():
    import options
    import input_int
    import exist_check

    transitions = {1:"はい",2:"いいえ"}

    options.options(transitions)
    num = input_int.input_int()
    while exist_check.exist_check(num,transitions) is False:
        print("適切な選択肢を選択してください")
        options.options(transitions)
        num = input_int.input_int()
    return num

"""a = yes_no_only()
print(a)"""

def yes_no_input(keyword):
    import options
    import input_int
    import exist_check
    transitions = {1:"はい",2:"いいえ"}

    if type(keyword) is not str:
        keyword = str(keyword)
    print("\n" + keyword + "でよろしいですか\n")
    options.options(transitions)
    num = input_int.input_int()
    while exist_check.exist_check(num,transitions) is False:
        print("適切な選択肢を選択してください")
        options.options(transitions)
        num = input_int.input_int()
    if num == 1:
        return True
    else:
        print("再度登録したい情報を入力してください：")
        return False

"""a = yes_no_input()
print(a)"""
