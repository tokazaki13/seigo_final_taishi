def pick_item(keyword):
    import connect
    import pymysql

    conn = connect.connect()
    cur = conn.cursor(pymysql.cursors.DictCursor)

    sql =  ("select 商品情報一覧テーブル.商品コード, 商品情報一覧テーブル.商品名, 商品詳細, 現在価格, (定価 - 現在価格) as '割引額', 分類名, CAST(在庫数 AS SIGNED) AS 在庫数,税率 from 商品情報一覧テーブル inner join 在庫テーブル on 商品情報一覧テーブル.商品コード = 在庫テーブル.商品コード where 取扱状況 = 0 and 在庫数 > 0 and 商品情報一覧テーブル.商品コード = %s")

    cur.execute(sql,keyword)

    conn.commit()
    result = cur.fetchone()
    cur.close()
    conn.close()

    return result
