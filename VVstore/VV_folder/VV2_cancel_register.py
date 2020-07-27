def VV2():
    import sys
    sys.path.append("/Users/User/Documents/seigo_final/customers/c_folder")
    import VV_show_orders
    import update_flags
    import get_orders
    import insert_canceled_orders
    import VV0_start_menu
    import yes_no
    import datetime
    import change_stock
    import options
    import input_int
    import exist_check
    import list_for_read
    import input_str
    import get_bite_count
    import check_fee


    print("\n～～～～～～～～～～～～～～～～～～\n\n【キャンセル登録】")

    transitions = {1:"キャンセル",2:"返品",3:"部分キャンセル",4:"部分返品",5:"戻る"}
    options.options(transitions)
    num = input_int.input_int()
    while exist_check.exist_check(num,transitions) is False:
        print("適切な選択肢を選択してください")
        options.options(transitions)
        num = input_int.input_int()

    if num == 1:
        bikou = "キャンセル"
    elif num == 2:
        bikou = "返品"
    elif num == 3:
        bikou = "部分キャンセル"
    elif num == 4:
        bikou = "部分返品"
    else:
        VV0_start_menu.VV0()

    result, order_id = VV_show_orders.VV_show_orders()
    if result is False:
        VV0_start_menu.VV0()

    """フラグUPDATE"""



    order_history,order_details_history,for_stock = get_orders.get_orders(order_id)
    ship_for_new = order_history[4]
    if order_history[6] == 1:
        print("キャンセル済みの受注IDが選択されているため、管理者メニューに戻ります")
        VV0_start_menu.VV0()
    update_flags.update_returned(order_id)
    order_history[6] = 1
    login_id = order_history[0]
    itemcode_list = []
    past_num_list = []
    past_list = []
    for code in order_details_history:
        itemcode = code[1]
        past_ordernum = code[3]
        past = -past_ordernum
        past_list.append(past)
        past_ordernum = str(past)
        past_ordernum = past_ordernum + "個"
        itemcode_list.append(itemcode)
        past_num_list.append(past_ordernum)
    code_num_dict = list_for_read.list_to_dict(itemcode_list,past_list)
    order_history.append(bikou)
    insert_canceled_orders.insert_orders(order_history)
    new_order_id = insert_canceled_orders.select_orders(login_id)

    for new_details in order_details_history:
        new_details[0] = new_order_id


    stock_date = datetime.date.today()
    bikou = bikou + "/受注ID" + str(order_id)
    for stocks in for_stock:
        stocks.insert(1,stock_date)
        stocks.insert(3,bikou)

    #在庫引当解除
    change_stock.change_stock(for_stock)

    insert_canceled_orders.insert_order_details(order_details_history)

    """
    一部なら、黒登録→カート追加に近いもの
    商品コード＆数量を取得
    それを繰り返す
    合計額を計算、配送料も計算
    それを元に、受注情報登録＆受注ID取得
    受注明細情報登録＆繰り返し
    """

    if num == 3 or num == 4:
        continue_to_change = 0
        black_details = []
        new_billing = []
        for_calc_ship = []
        new_for_stock = []
        while continue_to_change < 1:
            print("\n～～～～～～～～～～～～～～～～～～\n\n【キャンセル後受注情報登録】")
            print("～キャンセルした受注情報～")
            list_for_read.list_for_read(itemcode_list,past_num_list)
            print("部分キャンセル後の受注情報を登録してください")
            print("★注意★部分キャンセルではないが、部分キャンセルボタンを押してしまった場合のみ、「0」を入力しメインメニューに戻ってください！")
            print("商品コードを入力してください（英数字のみ入力）：")
            keyword = input_str.input_str()
            #半角で入力させる
            count = len(keyword)
            bite = get_bite_count.get_east_asian_width_count(keyword)
            if keyword == "0":
                VV0_start_menu.VV0()
            while bite != count or keyword not in itemcode_list:
                if bite != count:
                    print("英数字で入力されていません\n先ほどキャンセルした商品の商品コードを入力してください（英数字のみ入力）：")
                    keyword = input_str.input_str()
                    count = len(keyword)
                    bite = get_bite_count.get_east_asian_width_count(keyword)
                    if keyword == "0":
                        VV0_start_menu.VV0()
                elif keyword not in itemcode_list:
                    print("入力された商品はキャンセルされておりません")
                    print("～キャンセルした受注情報～")
                    list_for_read.list_for_read(itemcode_list,past_num_list)
                    print("\n先ほどキャンセルした商品の商品コードを入力してください（英数字のみ入力）：")
                    keyword = input_str.input_str()
                    if keyword == "0":
                        VV0_start_menu.VV0()
                    count = len(keyword)
                    bite = get_bite_count.get_east_asian_width_count(keyword)


            """
            keyword はOK
            """

            for temp_details in order_details_history:
                if temp_details[1] == keyword:
                    temp_num = code_num_dict.get(keyword)
                    temp_num_str = str(temp_num)
                    print("数量を入力してください\n★注意★　キャンセル前の数量以下で入力してください")
                    print("キャンセル前の数量：" + temp_num_str + "個")
                    new_num = input_int.input_int()
                    if new_num == 0:
                        VV0_start_menu.VV0()
                    while new_num > temp_num:
                        print("キャンセル前の数量以下で入力してください")
                        print("キャンセル前の数量：" + temp_num_str + "個")
                        new_num = input_int.input_int()
                        if new_num == 0:
                            VV0_start_menu.VV0()
                    temp_details[3] = new_num
                    temp_price = temp_details[4]
                    temp_price = int(temp_price)
                    temp_price = -temp_price
                    temp_details[4] = str(temp_price)

                    temp_price_tax = temp_details[5]
                    temp_price_tax = int(temp_price_tax)
                    temp_price_tax = -temp_price_tax
                    temp_details[5] = str(temp_price_tax)

                    price_num = temp_price * new_num
                    temp_details[6] = str(price_num)

                    price_num_tax = temp_price_tax * new_num
                    temp_details[7] = str(price_num_tax)

                    bikou = "部分キャンセル後再引当/" + login_id
                    new_stock = [keyword,stock_date,new_num,bikou]
                    new_for_stock.append(new_stock)

                    for_calc_ship.append(price_num)
                    new_billing.append(price_num_tax)
                    black_details.append(temp_details)
            itemcode_list.remove(keyword)
            past_list.remove(temp_num)
            a = temp_num_str + "個"
            past_num_list.remove(a)
            if len(itemcode_list) == 0:
                print("全ての商品を修正しました。\nキャンセル後の受注情報を登録します")
                continue_to_change += 1
            else:
                print("他に登録する商品はありますか")
                num = yes_no.yes_no_only()
                if num == 2:
                    continue_to_change += 1
        #ここ
        new_bill_amount = sum(new_billing)
        order_history[3] = str(new_bill_amount)
        ship = sum(for_calc_ship)
        #税抜合計が1万以下なら0円に変わる

        if ship >= 10000:
            order_history[4] = 0
        else:
            """
            ここに配送料SELECTを入れる
            """
            ship_fee = check_fee.check_fee(login_id)
            fee,tax = ship_fee.values()
            ship_fee = fee*(1+tax)
            ship_fee = round(ship_fee)
            order_history[4] = ship_fee
        order_history[6] = 0
        insert_canceled_orders.insert_orders(order_history)
        new_order_id = insert_canceled_orders.select_orders(login_id)

        for new_details in black_details:
            new_details[0] = new_order_id
        insert_canceled_orders.insert_order_details(black_details)


        change_stock.change_stock(new_for_stock)









    print("\n★引き続き、キャンセル登録を行いますか★\n")
    num = yes_no.yes_no_only()
    if num == 1:
        VV2()
    VV0_start_menu.VV0()
