def get_pw(login_id):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)
    #sql = ("SELECT password FROM customers WHERE login_id = %s")

    sql = ("SELECT password FROM 顧客履歴テーブル WHERE login_id = %s")

    cur.execute(sql,login_id)

    conn.commit()

    pw = cur.fetchall()


    cur.close()
    conn.close()

    for latest in pw:
        latest_pw = latest.get('password')

    return latest_pw
