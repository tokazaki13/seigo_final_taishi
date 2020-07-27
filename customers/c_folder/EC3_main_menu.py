#メインメニュー

def EC3_main_menu(login_id):
    import options
    import input_int
    import exist_check
    import EC0_start_menu
    import EC_exit
    import EC4_shopping_menu
    import EC11_read_customer_info
    import EC12_change_pw
    import EC13_show_history

    print("\n～～～～～～～～～～～～～～～～～～\n\n【ECメインメニュー】")

    transitions = {
    0:"ログアウト",
    1:"ショッピングカートメニュー",
    2:"会員情報表示",
    3:"パスワード変更",
    4:"購入履歴表示",
    5:"終了"}

    options.options(transitions)
    num = input_int.input_int()
    while exist_check.exist_check(num,transitions) is False:
        print("適切な選択肢を選択してください")
        options.options(transitions)
        num = input_int.input_int()

    if num == 0:
        EC0_start_menu.EC0_start_menu()
    elif num == 1:
        #ショッピングカートメニュー
        EC4_shopping_menu.EC4_shopping_menu(login_id)
    elif num == 2:
        #会員情報表示
        EC11_read_customer_info.EC11(login_id)
    elif num == 3:
        EC12_change_pw.EC12(login_id)
    elif num == 4:
        #購入履歴表示
        EC13_show_history.EC13(login_id)
    else:
        EC_exit.EC_exit()#終了


"""
elif num == 4:
    #購入履歴表示
    EC13(login_id)
    """
