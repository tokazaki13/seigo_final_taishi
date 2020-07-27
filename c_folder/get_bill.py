def get_bill(order_id):
    import connect
    import pymysql
    import datetime

    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)

    """出庫用明細出力時に税率が変更されると、新しい税率が請求書に記載されてしまう＋税計算は過去のものでやっている。なので、税率マスタを作成したら、ここの税率は税率履歴マスタから持ってくるようにする。もしくは商品履歴のIDを取得し、その履歴IDから税率を持ってくる"""

    sql = ("select 【編集禁止】受注明細テーブル（一覧表示用）.itemcode,【編集禁止】受注明細テーブル（一覧表示用）.name,商品情報一覧テーブル.商品詳細,ordernum, 【編集禁止】受注明細テーブル（一覧表示用）.price,【編集禁止】受注明細テーブル（一覧表示用）.price_with_tax,商品情報一覧テーブル.税率,【編集禁止】受注明細テーブル（一覧表示用）.total,【編集禁止】受注明細テーブル（一覧表示用）.total_with_tax,billing_amount,【編集禁止】受注テーブル（一覧表示用）.shipping_fee, order_date,【編集禁止】受注テーブル（一覧表示用）.name,顧客情報一覧テーブル.郵便番号,顧客情報一覧テーブル.住所,顧客情報一覧テーブル.電話番号,顧客情報一覧テーブル.メールアドレス from 【編集禁止】受注テーブル（一覧表示用）\
    inner join 【編集禁止】受注明細テーブル（一覧表示用） on 【編集禁止】受注テーブル（一覧表示用）.id = 【編集禁止】受注明細テーブル（一覧表示用）.order_id\
    inner join 顧客情報一覧テーブル on 【編集禁止】受注テーブル（一覧表示用）.login_id = 顧客情報一覧テーブル.ログインID\
    inner join 商品情報一覧テーブル on 【編集禁止】受注明細テーブル（一覧表示用）.itemcode = 商品情報一覧テーブル.商品コード\
    inner join 商品分類テーブル on 商品情報一覧テーブル.商品分類ID = 商品分類テーブル.id WHERE 【編集禁止】受注テーブル（一覧表示用）.id = %s")
    cur.execute(sql,order_id)

    conn.commit()

    result = cur.fetchall()


    cur.close()
    conn.close()
    

    order_details = []
    total_list = []
    total_tax_list = []
    for data in result:
        itemcode, item_name, author, ordernum, price, price_with_tax, tax, total, total_with_tax, billing_amount, shipping_fee, order_date, customer_name,zipcode,address,tel,mail_address = data.values()
        tax = float(tax) * 100
        tax = str(tax) + "%"
        total_list.append(int(total))
        total_tax_list.append(int(total_with_tax))
        price = "（" + price + "円）"
        price_with_tax = price_with_tax +"円"
        total = "（" + total + "円）"
        total_with_tax = total_with_tax +"円"
        order_details_list = [itemcode, item_name, author, price_with_tax,price, tax, ordernum, total_with_tax, total]
        order_details.append(order_details_list)

    sum_total = sum(total_list)
    sum_total_tax = sum(total_tax_list)
    sum_tax = sum_total_tax - sum_total

    due_date = order_date + datetime.timedelta(days=7)
    billdate = [order_date,due_date]
    bill_info = [customer_name,zipcode,address,tel,mail_address]
    return billing_amount,shipping_fee,order_details,billdate,bill_info,customer_name,sum_total,sum_total_tax,sum_tax
