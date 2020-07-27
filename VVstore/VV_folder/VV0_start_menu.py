#メインメニュー
def VV0():
    import sys
    sys.path.append("/Users/User/Documents/seigo_final/customers/c_folder")
    import options
    import input_int
    import exist_check
    import VV1_out_for_deliver
    import VV2_cancel_register
    import VV3_received
    import VV4_delivered
    import EC_exit

    print("\n～～～～～～～～～～～～～～～～～～\n\n【管理者用メインメニュー】")
    print("業務を選択してください")

    transitions = {1:"出庫用明細書出力",2:"キャンセル登録",3:"入金済み登録",4:"発送済み登録",5:"終了"}

    options.options(transitions)
    num = input_int.input_int()
    while exist_check.exist_check(num,transitions) is False:
        print("適切な選択肢を選択してください")
        options.options(transitions)
        num = input_int.input_int()

    if num == 1:
        VV1_out_for_deliver.VV1()
    elif num == 2:
        VV2_cancel_register.VV2()
    elif num == 3:
        VV3_received.VV3()
    elif num == 4:
        VV4_delivered.VV4()
    else:
        EC_exit.EC_exit()
