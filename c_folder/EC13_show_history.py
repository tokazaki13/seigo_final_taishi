def EC13(login_id):
    import get_history
    import item_info
    import EC3_main_menu

    print("\n～～～～～～～～～～～～～～～～～～\n\n【購入履歴表示】\n")
    order_history,order_details_history = get_history.get_history(login_id)
    column_1 = ["受注ID","受注日","請求額","配送料","キャンセル状況","配送状況"]
    column_2 = ["受注ID","商品コード","商品名","数量","税抜価格","税込価格","税抜小計","税込小計"]
    print("～購入概要～")
    item_info.item_info(order_history,column_1)
    print("\n\n\n")
    print("～購入内容詳細～")
    item_info.item_info(order_details_history,column_2)
    EC3_main_menu.EC3_main_menu(login_id)
