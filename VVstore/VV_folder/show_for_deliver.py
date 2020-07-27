def show_for_deliver():
    import sys
    sys.path.append("/Users/User/Documents/seigo_final/customers/c_folder")
    import input_int
    import get_order_id
    import get_order_data
    import item_info
    import yes_no
    import VV0_start_menu



    print("業務の対象とする受注IDを入力してください")
    print("★「0」を入力すると、前の画面に戻ります★")
    order_id = input_int.input_int()
    id_list = get_order_id.get_order_id()
    if order_id == 0:
        VV0_start_menu.VV0()
    while order_id not in id_list:
        print("存在しない受注IDが入力されています")
        print("業務の対象とする受注IDを入力してください")
        order_id = input_int.input_int()
        if order_id == 0:
            VV0_start_menu.VV0()

    order_history,order_details_history = get_order_data.get_order_data(order_id)
    column_1 = ["受注ID","顧客名","受注日","請求額","配送料","入金状況","キャンセル状況","配送状況"]
    column_2 = ["受注ID","商品コード","商品名","数量","税抜価格","税込価格","税抜小計","税込小計"]
    item_info.item_info(order_history,column_1)
    print("\n")
    item_info.item_info(order_details_history,column_2)

    id_list_for_deliver = get_order_id.get_order_id_for_deliver()
    if order_id not in id_list_for_deliver:
        print("\n\n～★注意★：未入金、発送済み、もしくはキャンセル済みの受注情報が選択されています!～\n")

    print("こちらの受注情報でよろしいですか")
    num = yes_no.yes_no_only()
    if num == 1:
        return True, order_id
    if num == 2:
        return False, order_id
