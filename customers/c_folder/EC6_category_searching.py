#商品カテゴリー検索
def EC6(login_id):
    import input_int
    import options
    import exist_check
    import select_categories
    import get_categories
    import check_select
    import EC4_shopping_menu

    print("\n～～～～～～～～～～～～～～～～～～\n\n【商品カテゴリー検索】")
    print("カテゴリーごとに商品表示を行います")
    print("★「0」を入力すると、前の画面に戻ります★")

    print("表示したい商品カテゴリーを入力してください：")

    #カテゴリーを取得
    transitions = get_categories.get_categories()

    options.options(transitions)
    num = input_int.input_int()
    if num == 0:
        EC4_shopping_menu.EC4_shopping_menu(login_id)
    while exist_check.exist_check(num,transitions) is False:
        print("適切な選択肢を選択してください")
        options.options(transitions)
        num = input_int.input_int()
        if num == 0:
            EC4_shopping_menu.EC4_shopping_menu(login_id)



    #カテゴリー検索
    result = select_categories.select_categories(num)
    #在庫状況＞０もいれる
    column = ["商品コード","商品名","商品詳細","税抜価格","割引額","税込価格","商品分類","在庫状況"]

    check_select.check_select(result,column)

    EC4_shopping_menu.EC4_shopping_menu(login_id)
