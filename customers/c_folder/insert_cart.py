#VV_dbのカートテーブルに登録する
def insert_cart(cart):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)


    cur.execute("USE vv_db")
    conn.commit()

    #データの挿入
    sql = "INSERT INTO 【一時保存用】ショッピングカートテーブル (itemcode,name,author,price,discounted,price_tax,num,total,total_tax,item_category,login_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cur.execute(sql,cart)

    conn.commit()
    cur.close()
    conn.close()

#カートテーブルを修正する
def update_cart(cart,login_id,keyword):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute("USE vv_db")
    conn.commit()

    delete_cart(login_id,keyword)
    #データの挿入
    sql = "INSERT INTO 【一時保存用】ショッピングカートテーブル (itemcode,name,author,price,discounted,price_tax,num,total,total_tax,item_category,login_id) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cur.execute(sql,cart)

    conn.commit()
    cur.close()
    conn.close()


def delete_cart(login_id,keyword):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)

    cur.execute("USE vv_db")
    conn.commit()

    #データの挿入
    sql = "DELETE FROM 【一時保存用】ショッピングカートテーブル where login_id = %s and itemcode = %s"

    cur.execute(sql,[login_id,keyword])

    conn.commit()
    cur.close()
    conn.close()
