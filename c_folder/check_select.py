def check_select(result,column):
    import item_info


    if len(result) == 0:
          print("\n現在取り扱っている商品はありません\n")
    else:
        print("\n※割引額が0でないものはセール対象商品です\n※定価から割引額を引いた価格を税抜価格で表示しています\n")

        l_list = []
        #リストにしてリストにappend?
        for dict_in in result:
            list = []
            itemcode, name, author, price, discounted, category, stock, tax = dict_in.values()
            price_tax = int(price) * (1 + float(tax))
            price_tax = round(price_tax)
            if stock > 5:
                stock = "有"
            list = [itemcode, name, author, price, discounted, price_tax, category, stock]
            l_list.append(list)
        item_info.item_info(l_list,column)

"""result = [{'itemcode': 'H2', 'name': 'エルマーの冒険', 'author': 'ルース・スタイルス・ガネット', '現在価格': '1080', '割引額': 120.0, '分類名': '書籍', '在庫数': 6, '税率': '0.1'}]
column = ["商品コード","商品名","商品詳細","税抜価格","割引額","税込価格","商品分類","在庫状況"]
check_select(result,column)

result = {}"""
