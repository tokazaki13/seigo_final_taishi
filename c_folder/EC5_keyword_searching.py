#商品キーワード検索
def EC5(login_id):
    import input_str
    import select_items
    import EC4_shopping_menu
    import check_select


    print("\n～～～～～～～～～～～～～～～～～～\n\n【商品キーワード検索】")
    print("キーワードをもとに、商品名・商品詳細検索をします")
    print("何も入力しない場合、取扱商品が全て表示されます")
    print("★「0」を入力すると、前の画面に戻ります★")
    print("例）キーワード：宮沢賢治\n検索結果：「注文の多い料理店」、「宮沢賢治特集」")
    print("検索キーワードを入力してください：")

    keyword = input_str.input_str()
    if keyword == "0":
        EC4_shopping_menu.EC4_shopping_menu(login_id)
    result = select_items.select_items(keyword)

    column = ["商品コード","商品名","商品詳細","税抜価格","割引額","税込価格","商品分類","在庫状況"]
    check_select.check_select(result,column)

    EC4_shopping_menu.EC4_shopping_menu(login_id)
