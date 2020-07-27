#VV_dbのcustomersテーブルに登録する
def insert_customers(customer_data):
    import connect
    import pymysql
    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)


    cur.execute("USE vv_db")
    conn.commit()

    #データの挿入
    insert_customer = "INSERT INTO 顧客履歴テーブル(login_id,name,tel,mail_address,zipcode,address,deliver_id,registered_date,password) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    cur.execute(insert_customer,customer_data)

    conn.commit()
    cur.close()
    conn.close()
    
