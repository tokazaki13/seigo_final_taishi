def check_itemcode(keyword):
    import connect
    import pymysql

    conn = connect.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    sql =  ("select * from 【一時保存用】ショッピングカートテーブル where login_id = %s")


    cur.execute(sql,keyword)

    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()

    return result


def get_cart_item(login_id,keyword):
    import connect
    import pymysql

    conn = connect.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    sql =  ("select * from 【一時保存用】ショッピングカートテーブル where login_id = %s and itemcode = %s")


    cur.execute(sql,[login_id,keyword])

    conn.commit()
    result = cur.fetchone()
    cur.close()
    conn.close()

    return result
"""a = get_cart_item("1","F2")
print(a)
b = get_cart_item("2","F2")
print(b)"""
