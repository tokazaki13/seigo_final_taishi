def get_history(login_id):
    import connect
    import pymysql

    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = ("SELECT 【編集禁止】受注テーブル（一覧表示用）.id, order_date, billing_amount, shipping_fee, itemcode, 【編集禁止】受注明細テーブル（一覧表示用）.name, ordernum, price, price_with_tax, total, total_with_tax, returned, delivered FROM 【編集禁止】受注テーブル（一覧表示用） inner join 【編集禁止】受注明細テーブル（一覧表示用） on 【編集禁止】受注テーブル（一覧表示用）.id = 【編集禁止】受注明細テーブル（一覧表示用）.order_id WHERE login_id = %s")
    cur.execute(sql,login_id)

    conn.commit()

    result = cur.fetchall()

    cur.close()
    conn.close()

    id_list = []
    order_history = []
    order_details_history = []


    for data in result:
        order_id, order_date, billing_amount, shipping_fee, itemcode, name, ordernum, price, price_with_tax, total, total_with_tax, returned, delivered = data.values()

        order_details_list = [order_id, itemcode, name, ordernum, price, price_with_tax, total, total_with_tax]
        order_details_history.append(order_details_list)

        if returned == 0:
            returned = "未"
        else:
            returned = "済"

        if delivered == 0:
            delivered = "未"
        else:
            delivered = "済"

        order_list = [order_id,order_date,billing_amount,shipping_fee,returned,delivered]
        if order_id not in id_list:
            order_history.append(order_list)
            id_list.append(order_id)


    return order_history,order_details_history

"""a,b = get_history("1")
print(a)
print(b)"""
