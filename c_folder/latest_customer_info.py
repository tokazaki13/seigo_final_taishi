def latest_customer_info(login_id):
    import connect
    import pymysql

    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)
    sql = ("SELECT 顧客名,電話番号,メールアドレス,郵便番号,住所,配送ID,登録日 FROM 顧客情報一覧テーブル WHERE ログインID = %s")
    cur.execute(sql,login_id)

    conn.commit()

    c_data = cur.fetchone()

    cur.close()
    conn.close()

    customer_data = []
    for data in c_data.values():
        customer_data.append(data)
    return customer_data
