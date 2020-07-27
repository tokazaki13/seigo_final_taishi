def get_order_id():
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT id FROM 【編集禁止】受注テーブル（一覧表示用）")

    conn.commit()
    id_dict = cur.fetchall()
    cur.close()
    conn.close()

    id_list = []
    for d in id_dict:
        for id in d.values():
            id_list.append(id)
    return id_list

def get_order_id_for_deliver():
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT 受注ID FROM 出庫待ちリスト")

    conn.commit()
    id_dict = cur.fetchall()
    cur.close()
    conn.close()

    id_list = []
    for d in id_dict:
        for id in d.values():
            id_list.append(id)
    return id_list
