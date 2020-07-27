#スタートメニュー
def EC0_start_menu():

    import options
    import input_int
    import exist_check
    import EC00_contacts
    import EC1_login
    import EC2_create_account
    import EC_exit

    print("～～～～～～～～～～～～～～～～～～\n\n【スタート画面】")
    print("VV商店 ECサイトへようこそ")

    transitions = {1:"ログイン",2:"新規会員登録",3:"お問い合わせ先表示",4:"終了"}

    options.options(transitions)

    num = input_int.input_int()
    while exist_check.exist_check(num,transitions) is False:
        print("適切な選択肢を選択してください")
        options.options(transitions)
        num = input_int.input_int()

    if num == 1:
        EC1_login.EC1_login()
    elif num == 2:
        EC2_create_account.EC2_create_account()
    elif num == 3:
        EC00_contacts.EC00()
    else:
        EC_exit.EC_exit()
