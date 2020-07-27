#商品選択
def EC7(login_id):
    import input_str
    import re
    import get_bite_count
    import pick_item
    import check_pick
    import input_int
    import EC4_shopping_menu
    import insert_cart
    import yes_no
    import check_itemcode
    import EC8_change_item
    import select_items
    print("\n～～～～～～～～～～～～～～～～～～\n\n【商品カート追加】")
    print("★「0」を入力すると、前の画面に戻ります★")

    print("カートに追加したい商品の商品コードを入力してください（英数字のみ入力）：")

    keyword = input_str.input_str()
    #半角で入力させる
    count = len(keyword)
    bite = get_bite_count.get_east_asian_width_count(keyword)
    itemcode_list = select_items.get_items()
    if keyword == "0":
        EC4_shopping_menu.EC4_shopping_menu(login_id)
    while bite != count or keyword not in itemcode_list:
        if bite != count:
            print("半角英数字で入力されていません\nカートに追加したい商品の商品コードを入力してください（英数字のみ入力）：")
            keyword = input_str.input_str()
            count = len(keyword)
            bite = get_bite_count.get_east_asian_width_count(keyword)
            if keyword == "0":
                EC4_shopping_menu.EC4_shopping_menu(login_id)
        elif keyword not in itemcode_list:
            print("入力された商品は取り扱いしておりません\nカートに追加したい商品の商品コードを入力してください（英数字のみ入力）：")
            keyword = input_str.input_str()
            if keyword == "0":
                EC4_shopping_menu.EC4_shopping_menu(login_id)
            count = len(keyword)
            bite = get_bite_count.get_east_asian_width_count(keyword)



    result = pick_item.pick_item(keyword)
    itemcode, name, author, price, discounted, category, stock, tax = result.values()

    """
    ここからIf文で条件分岐
        既に選択している商品コードを入力すると、True（同じ商品）を返す
        Trueなら数量変更機能と同じロジック
        Falseなら単なる選択ロジック
    """
    #カードにあるアイテムコードを取得
    itemcodes = check_itemcode.check_itemcode(login_id)
    code_list = []
    for itemcode in itemcodes:
        a = itemcode.get('itemcode')
        code_list.append(a)

    #入力されたアイテムコードがカートに存在すれば数量変更、しないならカート追加
    if keyword in code_list:
        print("\n\n既にショッピングカートに追加されている商品コードを選択されました\n商品数量変更画面に移動します")
        print("\n～～～～～～～～～～～～～～～～～～\n\n【商品数量変更】")

        EC8_change_item.EC8(login_id,keyword)

    else:

        print("購入したい数量を入力してください\n★注意★　最大購入数量は5個です")
        num = input_int.input_int()

        while num > 5 or num < 0 or num > stock:
            if num > 5:
                print("最大購入数量を超過しています")
            elif num > stock:
                print("入力された数量が在庫数を超過しています" + "\n現在の在庫数：" + str(stock))
                print("現在の在庫数以下の数値を入力してください")
            print("\n★注意★　最大購入数量は5個です")
            num = input_int.input_int()

        if num == 0:
            EC4_shopping_menu.EC4_shopping_menu(login_id)

        column = ["商品コード","商品名","商品詳細","税抜価格","割引額","税込価格","数量","税抜小計","税込小計","商品分類"]
        cart_info = check_pick.check_pick(result,column,num,login_id)
        cart_info.append(login_id)

        judge = yes_no.yes_no()

        if judge == 1:
            insert_cart.insert_cart(cart_info)
            print("ショッピングカートに追加しました")
            EC4_shopping_menu.EC4_shopping_menu(login_id)
        else:
            EC4_shopping_menu.EC4_shopping_menu(login_id)
