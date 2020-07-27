#数量変更
"""【数量変更機能】
現在の選択状況表示（数量変更なら、全商品：登録時変更なら、選択された商品）
選択数を確認させ、5個以上にならないようにする＋マイナスもOKにする。（在庫状況にも気を付ける）
入力された数値と既存の数値を足し算し、数量を判定
　
変更後の情報を表示し、YesNo確認
　変更後の数量がゼロなら、商品選択解除（DELETE）
　変更後の情報をUPDATE"""

def EC8(login_id,keyword):
    import get_bite_count
    import pick_item
    import check_pick
    import input_int
    import input_str
    import EC4_shopping_menu
    import yes_no
    import check_itemcode
    import item_info
    import yes_no
    import EC9_show_cart
    import insert_cart


    if len(keyword) == 0:
        print("\n～～～～～～～～～～～～～～～～～～\n\n【商品数量変更】")
        print("★「0」を入力すると、前の画面に戻ります★")

        print("数量変更したい商品の商品コードを入力してください（英数字のみ入力）：")



        itemcodes = check_itemcode.check_itemcode(login_id)
        code_list = []
        for itemcode in itemcodes:
            a = itemcode.get('itemcode')
            code_list.append(a)

        keyword = input_str.input_str()
        #半角で入力させる
        count = len(keyword)
        bite = get_bite_count.get_east_asian_width_count(keyword)

        if keyword == "0":
            EC9_show_cart.EC9(login_id)
        #英数字チェック
        #商品コード存在チェック
        while bite != count or keyword not in code_list:
            if keyword == "0":
                EC9_show_cart.EC9(login_id)
            print("英数字以外が入力されているか、カートにない商品コードを入力されています\n数量変更したい商品の商品コードを入力してください（英数字のみ入力）：")
            keyword = input_str.input_str()
            count = len(keyword)
            bite = get_bite_count.get_east_asian_width_count(keyword)



    #変更用の情報取得 在庫数のみでOK
    result = pick_item.pick_item(keyword)
    #stockのみ使用
    itemcode, name, author, price, discounted, category, stock, tax = result.values()

    #カート内の情報
    current_cart = check_itemcode.get_cart_item(login_id,keyword)
    #変数代入
    itemcode,name,author,price,discounted,price_tax,num,total,total_tax,item_category,login_id = current_cart.values()


    print("--------------------\n【数量変更説明】\n")
    print("＊戻る方法\n　　・「0」→「カート内表示画面」\n　　・「9」→「ショッピングカートメニュー」\n")
    print("＊商品の数量を減少させたいときは｢-1｣のように負の数を入力")
    print("＊例）カート内数量｢3｣のものに｢-1｣を入力すると、購入する商品の数量は｢2｣になります")
    print("\n＊★注意★　最大購入数量は5個です")
    print("\n＊変更後数量が｢0｣になるようにすると、商品をカート内から削除します\n--------------------")
    if stock <= 5:
        print("\n該当商品の在庫数：" + str(stock))
    print("\n追加・減少させたい数量を入力してください")
    new_num = input_int.input_int()
    if new_num == 0:
        EC9_show_cart.EC9(login_id)
    elif new_num == 9:
        EC4_shopping_menu.EC4_shopping_menu(login_id)

    while new_num+num > 5 or new_num+num > stock or num+new_num < 0:

        if new_num+num > 5:
            print("変更後数量が最大購入数量の5個を超過しています")
        elif new_num+num > stock:
            print("変更後数量が在庫数を超過しています" + "\n在庫数：" + str(stock))
        elif num+new_num < 0:
            print("変更後数量がマイナスになっています")

        #print("変更後数量："+str(new_num+num)+"\n")
        print("適切な数量を入力してください")
        print("\n追加・減少させたい数量を入力してください\n★注意★　最大購入数量は5個です")
        new_num = input_int.input_int()
        if new_num == 0:
            EC9_show_cart.EC9(login_id)
        elif new_num == 9:
            EC4_shopping_menu.EC4_shopping_menu(login_id)

    """
    カート内の数量←keyword+login_idから再セレクト
    該当商品の在庫数←resultから参照可能
    """
    if new_num+num == 0:
        #入力確認＆DELETE
        print("\n選択中の商品をカートから削除してもよろしいですか")
        judge = yes_no.yes_no_only()

        if judge == 1:
            insert_cart.delete_cart(login_id,itemcode)
            print("該当商品をカートから削除しました")
            EC9_show_cart.EC9(login_id)
        else:
            EC4_shopping_menu.EC4_shopping_menu(login_id)

    else:
        num = new_num+num
        total = int(price) * num
        total_tax = int(price_tax) * num
        cart =[[itemcode,name,author,price,discounted,price_tax,num,total,total_tax,item_category]]

        column = ["商品コード","商品名","商品詳細","税抜価格","割引額","税込価格","数量","税抜小計","税込小計","商品分類"]
        item_info.item_info(cart,column)



        cart =[itemcode,name,author,price,discounted,price_tax,num,total,total_tax,item_category]
        cart.append(login_id)

        print("【変更情報確認】")
        print("変更情報を確定してもよろしいですか")
        judge = yes_no.yes_no_only()

        if judge == 1:
            insert_cart.update_cart(cart,login_id,itemcode)
            print("カート内情報を変更しました")
            EC9_show_cart.EC9(login_id)
        else:
            EC4_shopping_menu.EC4_shopping_menu(login_id)
