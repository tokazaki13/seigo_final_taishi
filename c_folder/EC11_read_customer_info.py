#会員情報表示
def EC11(login_id):
    import options
    import list_for_read
    import EC3_main_menu
    import latest_customer_info

    customer_data = latest_customer_info.latest_customer_info(login_id)
    del customer_data[6]
    list = ["名前","電話番号","メールアドレス","郵便番号","住所","配送地域ID"]

    print("\n～～～～～～～～～～～～～～～～～～\n\n【会員情報表示画面】")
    print("\nパスワード以外の会員情報変更はVV商店までお問い合わせください\n")
    print("お問い合わせ情報はスタートメニューよりご確認いただけます")
    list_for_read.list_for_read(list,customer_data)


    #登録日は無理

    #配送地域IDの説明表示
    deliver = {2:"本島",3:"沖縄"}
    print("\n（配送地域ID一覧）")
    options.options(deliver)

    EC3_main_menu.EC3_main_menu(login_id)
