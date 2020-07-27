def select_loginid():
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)

    #一度使ったメールアドレスは変更されても使えないものとする
    cur.execute("SELECT login_id,mail_address FROM 顧客履歴テーブル")

    conn.commit()
    dict = cur.fetchall()
    cur.close()
    conn.close()

    id_list = []
    mail_list = []
    for d in dict:
        id, mail_address = d.values()
        id_list.append(id)
        mail_list.append(mail_address)
    return id_list,mail_list
#テーブル内のログインIDをリストにして返す

"""a,b = select_loginid()
print(a)
print(b)"""
