#ショッピングカートメニュー
def EC4_shopping_menu(login_id):
    import options
    import input_int
    import exist_check
    import EC_exit
    import EC3_main_menu
    import EC5_keyword_searching
    import EC6_category_searching
    import EC7_pick_item
    import EC9_show_cart



    print("\n～～～～～～～～～～～～～～～～～～\n\n【ショッピングカートメニュー】")

    transitions = {
    0:"戻る",
    1:"商品キーワード検索",
    2:"商品ジャンル別表示",
    3:"商品カート追加",
    4:"カート内情報表示（数量変更・購入画面）",
    5:"終了（★注意★：カート内情報は失われます）"}

    options.options(transitions)
    num = input_int.input_int()
    while exist_check.exist_check(num,transitions) is False:
        print("適切な選択肢を選択してください")
        options.options(transitions)
        num = input_int.input_int()

    if num == 0:
        EC3_main_menu.EC3_main_menu(login_id)
    elif num == 1:
        #商品キーワード検索
        EC5_keyword_searching.EC5(login_id)
    elif num == 2:
        #商品ジャンル別表示
        EC6_category_searching.EC6(login_id)
    elif num == 3:
        EC7_pick_item.EC7(login_id)
    elif num == 4:
        #カート内情報表示
        EC9_show_cart.EC9(login_id)
    else:
        EC_exit.EC_exit()#終了

"""elif num == 1:
    #商品キーワード検索
elif num == 2:
    #商品ジャンル別表示
elif num == 3:
    #商品カート追加
elif num == 4:
    #カート内情報表示"""
