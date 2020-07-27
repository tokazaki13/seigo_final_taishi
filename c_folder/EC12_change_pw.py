#パスワード変更
def EC12(login_id):
    import input_str
    import input_int
    import get_pw
    import if_same_check
    import EC3_main_menu
    import options
    import yes_no
    import insert_pw
    import check_count

    print("\n～～～～～～～～～～～～～～～～～～\n\n【パスワード変更画面】")
    print("★「0」を入力すると、前の画面に戻ります★")
    #パスワード照合
    print("\n現在のパスワードを入力してください：")
    password = input_str.input_str()
    pw = get_pw.get_pw(login_id)

    if password == "0":
        EC3_main_menu.EC3_main_menu(login_id)
    flag_3 = 0
    while flag_3 < 3:
        flag_3 = 0
        while check_count.check_half(password) is False:
            flag_3 = 0
            password = input_str.input_str()
            if password == "0":
                EC0_start_menu.EC0_start_menu()
        flag_3 += 1
        while check_count.check_count(password,16,1) is False:
            flag_3 = 0
            password = input_str.input_str()
            if password == "0":
                EC0_start_menu.EC0_start_menu()
        flag_3 += 1
        while if_same_check.if_same_check(password,pw) is False:
            flag_3 = 0
            print("パスワードが一致しません")
            print("\n現在パスワードを入力してください：")
            password = input_str.input_str()
            if password == "0":
                EC3_main_menu.EC3_main_menu(login_id)
        flag_3 += 1

    print("パスワードが一致しました")

    print("新しいパスワードを入力してください(16文字以内)")
    password = input_str.input_str()
    if password == "0":
        EC3_main_menu.EC3_main_menu(login_id)
    flag = 0

    while flag < 2:
        flag = 0
        while check_count.check_half(password) is False:
            flag = 0
            password = input_str.input_str()
            if password == "0":
                EC3_main_menu.EC3_main_menu(login_id)
        flag += 1
        while check_count.check_count(password,16,1) is False:
            flag = 0
            password = input_str.input_str()
            if password == "0":
                EC3_main_menu.EC3_main_menu(login_id)
        flag += 1

    print("もう一度新しいパスワードを入力してください(16文字以内)")
    new_pw_2 = input_str.input_str()
    if new_pw_2 == "0":
        EC3_main_menu.EC3_main_menu(login_id)
    while flag < 3:
        flag = 0
        while check_count.check_half(new_pw_2) is False:
            flag = 0
            new_pw_2 = input_str.input_str()
            if new_pw_2 == "0":
                EC3_main_menu.EC3_main_menu(login_id)
        flag += 1
        while check_count.check_count(new_pw_2,16,1) is False:
            flag = 0
            new_pw_2 = input_str.input_str()
            if new_pw_2 == "0":
                EC3_main_menu.EC3_main_menu(login_id)
        flag += 1
        while if_same_check.if_same_check(password,new_pw_2) is False:
            flag = 0
            print("パスワードが一致しません")
            print("もう一度新しいパスワードを入力してください：")
            new_pw_2 = input_str.input_str()
            if new_pw_2 == "0":
                EC3_main_menu.EC3_main_menu(login_id)
        flag += 1
    print("---------------------------\n新しいパスワードが一致しました")
    num = yes_no.yes_no()

    if num == 1:
        insert_pw.insert_pw(login_id,new_pw_2)
        print("パスワード変更が完了しました")
        EC3_main_menu.EC3_main_menu(login_id)
    else:
        EC3_main_menu.EC3_main_menu(login_id)




    """
    ログインに近い処理
    　まずPWを持ってきて、PW入力させて照合
    OKなら、新PWを入力させる
    確定処理
    登録
    """
