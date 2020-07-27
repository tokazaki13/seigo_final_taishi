def check_fee(keyword):
    import connect
    import pymysql

    conn = connect.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    sql =  ("select fee,tax from 配送テーブル inner join 顧客情報一覧テーブル on 配送テーブル.id = 顧客情報一覧テーブル.配送ID where ログインID = %s")


    cur.execute(sql,keyword)

    conn.commit()
    result = cur.fetchone()
    cur.close()
    conn.close()


    return result
"""a = check_fee("1")
print(a)
"""
