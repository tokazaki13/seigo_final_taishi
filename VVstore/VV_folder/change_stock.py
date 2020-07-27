def change_stock(stock_info):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)


    cur.execute("USE vv_db")
    conn.commit()


    for stock_num in stock_info:
        num = stock_num[2]


    if num < 0:
        #入庫
        for stock_num in stock_info:
            num = stock_num[2]
            in_num = -num
            stock_num[2] = in_num
        sql = "INSERT INTO 入出庫履歴テーブル (itemcode,stock_date,in_num,bikou) VALUES(%s,%s,%s,%s)"
    else:
        #出庫
        sql = "INSERT INTO 入出庫履歴テーブル (itemcode,stock_date,out_num,bikou) VALUES(%s,%s,%s,%s)"

    for stock in stock_info:
        cur.execute(sql,stock)

    conn.commit()
    cur.close()
    conn.close()
