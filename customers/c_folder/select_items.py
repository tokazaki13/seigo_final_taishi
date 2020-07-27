def select_items(keyword):
    import connect
    import pymysql

    conn = connect.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)


    keyword = "%" + keyword + "%"
    sql =  ("select 商品情報一覧テーブル.商品コード, 商品情報一覧テーブル.商品名, 商品詳細, 現在価格, (定価 - 現在価格) as '割引額', 分類名, CAST(在庫数 AS SIGNED) AS 在庫数,税率 from 商品情報一覧テーブル inner join 在庫テーブル on 商品情報一覧テーブル.商品コード = 在庫テーブル.商品コード where 取扱状況 = 0 and 在庫数 > 0 and (商品詳細 LIKE %s or 商品情報一覧テーブル.商品名 LIKE %s)")



    cur.execute(sql,[keyword,keyword])

    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()

    return result
"""a = select_items("one")
print(a)"""

def get_items():
    import connect
    import pymysql

    conn = connect.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)


    sql =  ("select 商品情報一覧テーブル.商品コード from 商品情報一覧テーブル inner join 在庫テーブル on 商品情報一覧テーブル.商品コード = 在庫テーブル.商品コード where 取扱状況 = 0 and 在庫数 > 0")



    cur.execute(sql)

    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()

    itemcode_list = []
    for a in result:
        itemcode = a.get('商品コード')
        itemcode_list.append(itemcode)

    return itemcode_list

"""a = get_items()
print(a)"""





"""
あいまい検索
sql =  ("select itemcode, name, author, 現在価格, (price - 現在価格) as '割引額', 分類名 from 商品情報一覧テーブル where delete_flag = 0 and name LIKE '%%s%'")
"""
