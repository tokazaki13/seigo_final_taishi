
def get_order_data(order_id):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = ("SELECT 【編集禁止】受注テーブル（一覧表示用）.id, 【編集禁止】受注テーブル（一覧表示用）.name, order_date, billing_amount, shipping_fee, itemcode, 【編集禁止】受注明細テーブル（一覧表示用）.name, ordernum, price, price_with_tax, total, total_with_tax, received, returned, delivered FROM 【編集禁止】受注テーブル（一覧表示用） inner join 【編集禁止】受注明細テーブル（一覧表示用） on 【編集禁止】受注テーブル（一覧表示用）.id = 【編集禁止】受注明細テーブル（一覧表示用）.order_id WHERE order_id = %s")

    cur.execute(sql,order_id)

    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()

    id_list = []
    order_history = []
    order_details_history = []
    for data in result:
        order_id, customer_name, order_date, billing_amount, shipping_fee, itemcode, name, ordernum, price, price_with_tax, total, total_with_tax, received, returned, delivered = data.values()

        order_details_list = [order_id, itemcode, name, ordernum, price, price_with_tax, total, total_with_tax]
        order_details_history.append(order_details_list)

        if received == 0:
            received = "未"
        else:
            received = "済"

        if returned == 0:
            returned = "未"
        else:
            returned = "済"

        if delivered == 0:
            delivered = "未"
        else:
            delivered = "済"

        order_list = [order_id,customer_name,order_date,billing_amount,shipping_fee,received,returned,delivered]
        if order_id not in id_list:
            order_history.append(order_list)
            id_list.append(order_id)

    return order_history,order_details_history
