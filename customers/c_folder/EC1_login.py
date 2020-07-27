
def EC1_login():
    import input_str
    import select_loginid
    import exist_check
    import get_pw
    import if_same_check
    import EC3_main_menu
    import EC0_start_menu
    import check_count



    print("\n～～～～～～～～～～～～～～～～～～\n\n【ログイン画面】")
    print("★「0」を入力すると、前の画面に戻ります★")
    #ログインID照合
    id_dict, mail_list = select_loginid.select_loginid()
    flag = 0
    flag_2 = 0
    flag_3 = 0
    while flag < 2:
        flag = 0
        flag_2 = 0
        flag_3 = 0
        print("ログインIDを入力してください：")
        login_id = input_str.input_str()
        if login_id == "0":
            EC0_start_menu.EC0_start_menu()
        while flag_2 < 2:
            flag_2 = 0
            while check_count.check_count(login_id,8,1) is False:
                flag_2 = 0
                login_id = input_str.input_str()
                if login_id == "0":
                    EC0_start_menu.EC0_start_menu()
            flag_2 += 1
            while check_count.check_half(login_id) is False:
                flag_2 = 0
                login_id = input_str.input_str()
                if login_id == "0":
                    EC0_start_menu.EC0_start_menu()
            flag_2 += 1

        if exist_check.exist_check(login_id,id_dict) is True:
            pw = get_pw.get_pw(login_id)
            flag += 1
        else:
            pw = None

        #パスワード照合
        print("\nパスワードを入力してください：")
        password = input_str.input_str()
        if password == "0":
            EC0_start_menu.EC0_start_menu()
        while flag_3 < 2:
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
        if if_same_check.if_same_check(password,pw) is True:
            flag += 1
        if flag != 2:
            print("IDかパスワードに誤りがあります\n再度ログイン情報を入力してください\n")



    print("ログイン成功")
    #EC3_main_menu に画面遷移
    EC3_main_menu.EC3_main_menu(login_id)
