def check_cart(result,column):
    import item_info





    print("\n※定価から割引額を引いた価格を税抜き価格で表示しています\n")
    print("税抜合計で10000円以上お買い上げいただきますと、配送料が無料になります")

    l_list = []
    #リストにしてリストにappend?
    for dict_in in result:
        list = []
        itemcode,name,author,price,discounted,price_tax,num,total,total_tax,item_category,login_id = dict_in.values()

        list = [itemcode,name,author,price,discounted,price_tax,num,total,total_tax,item_category]
        l_list.append(list)
    item_info.item_info(l_list,column)


#EC10で使用
def show_cart(result,column,fee,tax):
    import item_info
    import yes_no
    import EC9_show_cart


    if len(result) == 0:
          print("\n現在カート内に追加された商品はありません\n")
    else:


        l_list = []
        #リストにしてリストにappend?
        total_list = []
        total_tax_list = []
        total_discounted = []

        for dict_in in result:
            list = []
            itemcode,name,author,price,discounted,price_tax,num,total,total_tax,item_category,login_id = dict_in.values()

            list = [itemcode,name,author,price,discounted,price_tax,num,total,total_tax,item_category]
            l_list.append(list)

            total_list.append(int(total))
            total_tax_list.append(int(total_tax))
            d = int(discounted) * num
            total_discounted.append(d)
        item_info.item_info(l_list,column)

        sum_total = sum(total_list)
        sum_tax = sum(total_tax_list)
        sum_discounted = sum(total_discounted)

        print("税込合計（税抜合計）：" + str(sum_tax) + "円（" + str(sum_total) + "）円")
        print("合計割引額　　　　　　　　　：" + str(sum_discounted) + "円")
        if sum_total >= 10000:
            shipping_fee = 0
            fee = 0
            print("　（税抜合計が10000円以上なため、配送料を無料とさせていただきます）")
        else:
            shipping_fee = fee*(1+tax)
            shipping_fee = round(shipping_fee)
        print("税込配送料（税抜配送料）　　：" + str(shipping_fee) + "円（" + str(fee) + "）円")
        billing = sum_tax + shipping_fee
        print("税込総額　　　　　　　　　　：" + str(billing) + "円")


        order = [login_id,billing,shipping_fee]
        #インサートファイルで order.insert(1,customer_name)
        #インサートファイルで order.append(tel)
        #インサートファイルで order.append(mail_address)

        #インサートファイルで order_details.insert(0,order_id)


        print("【購入確認】")
        print("購入の確定をします")
        judge = yes_no.yes_no_only()

        if judge == 1:
            print("購入が確定しました")
            return order
        else:
            EC9_show_cart.EC9(login_id)


#bite = get_bite_count.get_east_asian_width_count(keyword)
