def get_categories():
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)
    cur.execute("SELECT name FROM 商品分類テーブル")

    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()

    category_list = []
    for d in result:

        c = d.get("name")
        category_list.append(c)


    #辞書作成
    category_dict = {}
    int = 1
    for a in category_list:

        category_dict[int] = a
        int += 1

    #print(category_dict)
    return category_dict

    #return id_list,category_list

#テーブル内のログインIDをリストにして返す
