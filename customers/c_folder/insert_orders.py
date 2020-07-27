#VV_dbのORDERに登録する
def insert_orders(cart):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)


    cur.execute("USE vv_db")
    conn.commit()

    #データの挿入
    sql = "INSERT INTO 【編集禁止】受注テーブル（一覧表示用） (login_id,name,billing_amount,shipping_fee,tel,mail_address) VALUES(%s,%s,%s,%s,%s,%s)"

    cur.execute(sql,cart)

    conn.commit()
    cur.close()
    conn.close()

def select_orders(login_id):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute("USE vv_db")
    conn.commit()

    #データの挿入
    sql = ("SELECT MAX(id) FROM 【編集禁止】受注テーブル（一覧表示用） WHERE login_id = %s")


    cur.execute(sql, login_id)

    conn.commit()

    result = cur.fetchone()

    cur.close()
    conn.close()
    return result


def insert_order_details(cart):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)


    cur.execute("USE vv_db")
    conn.commit()

    #データの挿入
    sql = "INSERT INTO 【編集禁止】受注明細テーブル（一覧表示用） (order_id,itemcode,name,ordernum,price,price_with_tax,total,total_with_tax) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"

    cur.execute(sql,cart)

    conn.commit()
    cur.close()
    conn.close()

def delete_cart(login_id):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute("USE vv_db")
    conn.commit()

    #データの挿入
    sql = "DELETE FROM 【一時保存用】ショッピングカートテーブル where login_id = %s"

    cur.execute(sql,login_id)

    conn.commit()
    cur.close()
    conn.close()
