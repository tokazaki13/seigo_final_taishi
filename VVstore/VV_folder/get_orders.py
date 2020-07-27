
def get_orders(order_id):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = ("SELECT login_id,【編集禁止】受注テーブル（一覧表示用）.name,order_date,billing_amount,shipping_fee,received,returned,canceled_id,tel,mail_address,itemcode,【編集禁止】受注明細テーブル（一覧表示用）.name,ordernum,price,price_with_tax,total,total_with_tax FROM 【編集禁止】受注テーブル（一覧表示用） inner join 【編集禁止】受注明細テーブル（一覧表示用） on 【編集禁止】受注テーブル（一覧表示用）.id = 【編集禁止】受注明細テーブル（一覧表示用）.order_id WHERE order_id = %s")

    cur.execute(sql,order_id)

    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()


    order_details_history = []
    for_stock = []
    for data in result:
        login_id,c_name,order_date,billing_amount,shipping_fee,received,returned,canceled_id,tel,mail_address,itemcode,i_name,ordernum,price,price_with_tax,total,total_with_tax = data.values()



        minus_num = -ordernum

        price = int(price)
        price = -price
        price = str(price)
        price_with_tax = int(price_with_tax)
        price_with_tax = -price_with_tax
        price_with_tax = str(price_with_tax)
        total = int(total)
        total = -total
        total = str(total)
        total_with_tax = int(total_with_tax)
        total_with_tax = -total_with_tax
        total_with_tax = str(total_with_tax)

        stock = [itemcode,minus_num]
        for_stock.append(stock)

        order_details_list = [order_id,itemcode,i_name,minus_num,price,price_with_tax,total,total_with_tax]
        order_details_history.append(order_details_list)


    canceled_id = order_id
    shipping_fee = -shipping_fee
    billing_amount = int(billing_amount)
    billing_amount = -billing_amount
    billing_amount = str(billing_amount)
    order_list = [login_id,c_name,order_date,billing_amount,shipping_fee,received,returned,canceled_id,tel,mail_address]


    return order_list,order_details_history,for_stock
