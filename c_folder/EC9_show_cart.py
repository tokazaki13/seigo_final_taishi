#カート内表示
def EC9(login_id):
    import check_itemcode
    import check_cart
    import options
    import input_int
    import exist_check
    import EC_exit
    import EC4_shopping_menu
    import EC8_change_item
    import EC10_buy

    print("\n～～～～～～～～～～～～～～～～～～\n\n【カート内表示画面】")

    column = ["商品コード","商品名","商品詳細","税抜価格","割引額","税込価格","数量","税抜小計","税込小計","商品分類"]
    cart = check_itemcode.check_itemcode(login_id)
    if len(cart) == 0:
        print("カートに追加された商品はありません。\n商品を追加してください")
        EC4_shopping_menu.EC4_shopping_menu(login_id)
    check_cart.check_cart(cart,column)

    transitions = {
    0:"戻る",
    1:"購入確認",
    2:"数量変更",
    3:"終了"}


    options.options(transitions)
    num = input_int.input_int()
    while exist_check.exist_check(num,transitions) is False:
        print("適切な選択肢を選択してください")
        options.options(transitions)
        num = input_int.input_int()

    if num == 0:
        EC4_shopping_menu.EC4_shopping_menu(login_id)
    elif num == 1:
        #購入確認画面
        EC10_buy.EC10(login_id)
    elif num == 2:
        #数量変更
        keyword = ""
        EC8_change_item.EC8(login_id,keyword)
    else:
        EC_exit.EC_exit()#終了
