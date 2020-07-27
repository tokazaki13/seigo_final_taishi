def check_pick(result,column,num,login_id):
    import item_info
    import EC7_pick_item


    if result == None:
        print("\n現在取り扱っている商品はありません\n")
    else:
        print("\n※定価から割引額を引いた価格を税抜き価格で表示しています\n")

        l_list = []
        #リストにしてリストにappend?

        itemcode, name, author, price, discounted, category, stock, tax = result.values()


        
        price_tax = int(price) * (1 + float(tax))
        price_tax = round(price_tax)
        total = int(price)*num
        total_tax = price_tax*num
        list = [itemcode, name, author, price, discounted, price_tax, num, total, total_tax, category]
        l_list.append(list)
        item_info.item_info(l_list,column)
        return list
