#新規会員登録
def EC2_create_account():
    import input_str
    import input_int
    import options
    import exist_check
    import select_loginid
    import EC0_start_menu
    import insert_customers
    import list_for_read
    import yes_no
    import datetime
    import check_count
    import if_same_check



    id_list,mail_list = select_loginid.select_loginid()
    print("\n～～～～～～～～～～～～～～～～～～\n\n【新規会員登録画面】")
    print("★「0」を入力すると、前の画面に戻ります★")
    list = ["ログインID","名前","電話番号","メールアドレス","郵便番号","住所","配送地域ID"]
    customer_data = []


    #文字列入力 16
    print("------------------\n名前を入力してください(16文字以内)：")
    name = input_str.input_str()
    if name == "0":
        EC0_start_menu.EC0_start_menu()
    flag = 0
    while flag < 2:
        flag = 0
        while check_count.check_count(name,16,1) is False:
            name = input_str.input_str()
            if name == "0":
                EC0_start_menu.EC0_start_menu()
        flag += 1
        if yes_no.yes_no_input(name) is True:
            flag += 1
        else:
            name = input_str.input_str()
            if name == "0":
                EC0_start_menu.EC0_start_menu()
    customer_data.append(name)

    #数値入力 10-11
    print("------------------\n電話番号を入力してください(10文字～11文字)：")
    print("最初の0は省略してください\n例）「090」は「90]と入力")
    tel = input_int.input_int()
    if tel == 0:
        EC0_start_menu.EC0_start_menu()
    tel = "0" + str(tel)
    flag = 0
    while flag < 2:
        flag = 0
        while check_count.check_count(tel,11,10) is False:
            tel = input_int.input_int()
            if tel == 0:
                EC0_start_menu.EC0_start_menu()
            tel = "0" + str(tel)
        flag += 1
        if yes_no.yes_no_input(tel) is True:
            flag += 1
        else:
            tel = input_int.input_int()
            if tel == 0:
                EC0_start_menu.EC0_start_menu()
            tel = "0" + str(tel)


    customer_data.append(tel)

    #文字列入力/半角英数字 128
    print("------------------\nメールアドレスを入力してください(128文字以内)：")
    mail_address = input_str.input_str()
    if mail_address == "0":
        EC0_start_menu.EC0_start_menu()

    flag = 0
    while flag < 4:
        flag = 0
        while check_count.check_count(mail_address,128,1) is False:
            flag = 0
            mail_address = input_str.input_str()
            if mail_address == "0":
                EC0_start_menu.EC0_start_menu()
        flag += 1
        #SELECTして、ログインIDリストを作成→存在チェックで
        while exist_check.exist_check(mail_address,mail_list) is True:
            flag = 0
            print("入力されたメールアドレスは既に使用されています")
            print("別のメールアドレスを入力してください：")
            mail_address = input_str.input_str()
            if mail_address == "0":
                EC0_start_menu.EC0_start_menu()
        flag += 1
        while check_count.check_half(mail_address) is False:
            flag = 0
            mail_address = input_str.input_str()
            if mail_address == "0":
                EC0_start_menu.EC0_start_menu()
        flag += 1
        if yes_no.yes_no_input(mail_address) is True:
            flag += 1
        else:
            mail_address = input_str.input_str()
            if mail_address == "0":
                EC0_start_menu.EC0_start_menu()
    customer_data.append(mail_address)

    #数値入力 7 ハイフンなし
    print("------------------\n郵便番号を入力してください(7文字,ハイフンなし)")
    zipcode = input_int.input_int()
    if zipcode == 0:
        EC0_start_menu.EC0_start_menu()
    zipcode = str(zipcode)

    flag = 0
    while flag < 2:
        flag = 0
        while check_count.check_count(zipcode,7,7) is False:
            zipcode = input_int.input_int()
            if zipcode == 0:
                EC0_start_menu.EC0_start_menu()
            zipcode = str(zipcode)
        flag += 1
        if yes_no.yes_no_input(zipcode) is True:
            flag += 1
        else:
            zipcode = input_int.input_int()
            if zipcode == 0:
                EC0_start_menu.EC0_start_menu()
            zipcode = str(zipcode)


    customer_data.append(zipcode)

    #文字列入力 64
    print("------------------\n住所を入力してください(64文字以内)：")
    address = input_str.input_str()
    if address == "0":
        EC0_start_menu.EC0_start_menu()

    flag = 0
    while flag < 2:
        flag = 0
        while check_count.check_count(address,64,3) is False:
            address = input_str.input_str()
            if address == "0":
                EC0_start_menu.EC0_start_menu()
        flag += 1
        if yes_no.yes_no_input(address) is True:
            flag += 1
        else:
            address = input_str.input_str()
            if address == "0":
                EC0_start_menu.EC0_start_menu()

    customer_data.append(address)


    #数値入力
    print("------------------")
    deliver = {1:"本島",2:"沖縄"}
    options.options(deliver)
    print("配送地域IDを入力してください")
    deliver_id = input_int.input_int()
    if deliver_id == 0:
        EC0_start_menu.EC0_start_menu()
    flag = 0
    while flag < 2:
        flag = 0
        while exist_check.exist_check(deliver_id,deliver) is False:
            print("適切な選択肢を選択してください")
            deliver = {1:"本島",2:"沖縄"}
            options.options(deliver)
            print("配送地域IDを入力してください")
            deliver_id = input_int.input_int()
            if deliver_id == 0:
                EC0_start_menu.EC0_start_menu()
        flag += 1
        if deliver_id == 1:
            area = "本島"
        else:
            area = "沖縄"

        if yes_no.yes_no_input(area) is True:
            flag += 1
        else:
            deliver = {1:"本島",2:"沖縄"}
            options.options(deliver)
            print("配送地域IDを入力してください")
            deliver_id = input_int.input_int()
            if deliver_id == 0:
                EC0_start_menu.EC0_start_menu()
    customer_data.append(deliver_id)


    #文字列入力/半角英数字 8
    print("------------------\nログインIDを入力してください(8文字以内)：")
    login_id = input_str.input_str()
    if login_id == "0":
        EC0_start_menu.EC0_start_menu()
    flag = 0
    flag_2 = 0
    while flag_2 < 1:
        flag_2 = 0
        flag = 0
        while flag < 3:
            flag = 0
            while check_count.check_count(login_id,8,1) is False:
                login_id = input_str.input_str()
                if login_id == "0":
                    EC0_start_menu.EC0_start_menu()
            flag += 1
            #SELECTして、ログインIDリストを作成→存在チェックで
            while exist_check.exist_check(login_id,id_list) is True:
                flag = 0
                print("入力されたログインIDは既に使用されています")
                print("別のログインIDを入力してください：")
                login_id = input_str.input_str()
                if login_id == "0":
                    EC0_start_menu.EC0_start_menu()
            flag += 1
            while check_count.check_half(login_id) is False:
                flag = 0
                login_id = input_str.input_str()
                if login_id == "0":
                    EC0_start_menu.EC0_start_menu()
            flag += 1
        if yes_no.yes_no_input(login_id) is True:
            flag_2 += 1
        else:
            print("------------------\nログインIDを入力してください(8文字以内)：")
            login_id = input_str.input_str()
            if login_id == "0":
                EC0_start_menu.EC0_start_menu()
    customer_data.insert(0,login_id)

    #文字列入力/半角英数字 16
    print("------------------\nパスワードを入力してください(16文字以内)：")
    password = input_str.input_str()
    if password == "0":
        EC0_start_menu.EC0_start_menu()
    flag = 0

    while flag < 2:
        flag = 0
        while check_count.check_half(password) is False:
            flag = 0
            password = input_str.input_str()
            if password == "0":
                EC0_start_menu.EC0_start_menu()
        flag += 1
        while check_count.check_count(password,16,1) is False:
            flag = 0
            password = input_str.input_str()
            if password == "0":
                EC0_start_menu.EC0_start_menu()
        flag += 1

    print("もう一度パスワードを入力してください(16文字以内)")
    new_pw_2 = input_str.input_str()
    if new_pw_2 == "0":
        EC0_start_menu.EC0_start_menu()
    while flag < 3:
        flag = 0
        while check_count.check_half(new_pw_2) is False:
            flag = 0
            new_pw_2 = input_str.input_str()
            if new_pw_2 == "0":
                EC0_start_menu.EC0_start_menu()
        flag += 1
        while check_count.check_count(new_pw_2,16,1) is False:
            flag = 0
            new_pw_2 = input_str.input_str()
            if new_pw_2 == "0":
                EC0_start_menu.EC0_start_menu()
        flag += 1
        while if_same_check.if_same_check(password,new_pw_2) is False:
            flag = 0
            print("パスワードが一致しません")
            print("もう一度パスワードを入力してください：")
            new_pw_2 = input_str.input_str()
            if new_pw_2 == "0":
                EC0_start_menu.EC0_start_menu()
        flag += 1
    print("---------------------------\nパスワードが一致しました")

    print("\n～～～～～～～～～～～～～～～～～～\n\n【入力情報確認】")

    list_for_read.list_for_read(list,customer_data)
    if deliver_id == 1:
        area = "本島"
        print("配送地域：" + area)
    else:
        area = "沖縄"
        print("配送地域：" + area)


    #トランジション　はい、いいえを入れる
    num = yes_no.yes_no()

    if num == 1:
        registered_date = datetime.date.today()

        customer_data.insert(7,registered_date)
        customer_data[6] += 1
        customer_data.append(password)
        insert_customers.insert_customers(customer_data)
        print("会員登録が完了しました")
        EC0_start_menu.EC0_start_menu()
    else:
        EC2_create_account()
