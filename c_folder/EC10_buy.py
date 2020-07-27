def EC10(login_id):
    import check_itemcode
    import check_cart
    import check_fee
    import latest_customer_info
    import insert_orders
    import get_order_details
    import get_bill
    import EC3_main_menu
    import out_bill
    import datetime
    import sys
    sys.path.append("/Users/User/Documents/seigo_final/VVstore/VV_folder")
    import change_stock

    print("\n～～～～～～～～～～～～～～～～～～\n\n【購入確認】")

    delivers = check_fee.check_fee(login_id)
    fee = delivers.get('fee')
    tax = delivers.get('tax')



    column = ["商品コード","商品名","商品詳細","税抜価格","割引額","税込価格","数量","税抜小計","税込小計","商品分類"]
    cart = check_itemcode.check_itemcode(login_id)
    order = check_cart.show_cart(cart,column,fee,tax)

    customer_list = latest_customer_info.latest_customer_info(login_id)
    customer_name = customer_list[0]
    mail_address = customer_list[2]
    tel = customer_list[1]


    order.insert(1,customer_name)
    order.append(tel)
    order.append(mail_address)
    #orderリストを受注テーブルにインサート
    insert_orders.insert_orders(order)
    #インサートしたorderのIDを取得
    order_id = insert_orders.select_orders(login_id)
    order_id = order_id.get('MAX(id)')
    #order_idをorder_detailsリストに追加
    #インサートファイルで order_details.insert(0,order_id)
    order_details_list = get_order_details.get_order_details(cart,order_id)

    #在庫引当用リスト(itemcode,stock_date,ordernum,bikou)
    stock_date = datetime.date.today()
    bikou = "出庫" + "/" + login_id
    stock_list = []
    #order_detailsリストを受注明細テーブルにインサート
    for order_details in order_details_list:
        insert_orders.insert_order_details(order_details)

        stock_info = [stock_date,bikou]
        itemcode = order_details[1]
        out_num = order_details[3]
        stock_info.insert(0,itemcode)
        stock_info.insert(2,out_num)
        stock_list.append(stock_info)

    #ショッピングカートをクリア
    insert_orders.delete_cart(login_id)

    #在庫引当
    change_stock.change_stock(stock_list)

    #order_idをもとに請求書出力
    billing_amount,shipping_fee,order_details,billdate,bill_info,customer_name,sum_total,sum_total_tax,sum_tax = get_bill.get_bill(order_id)

    column = ["商品番号","商品名","商品詳細","税込単価","（税抜単価）","税率","数量","税込小計","（税抜小計）"]
    out_bill.out_bill(order_details,column,billing_amount,shipping_fee,billdate,bill_info,customer_name,sum_total,sum_total_tax,sum_tax)

    #ショッピングカートメニューorメインメニューに戻る
    EC3_main_menu.EC3_main_menu(login_id)
