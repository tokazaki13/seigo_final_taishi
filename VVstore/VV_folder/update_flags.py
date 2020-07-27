
def update_delivered(order_id):
    import pymysql.cursors

    try:
        import pymysql
        pymysql.install_as_MySQLdb()
    except ImportError:
        pass

    conn = pymysql.connect(
     user = "root",
     passwd = "seigo2017",
     host = "localhost",
     db = "vv_db"
    )


    cur = conn.cursor()

    sql = ("UPDATE 【編集禁止】受注テーブル（一覧表示用） SET delivered = 1 WHERE id = %s")
    cur.execute(sql,order_id)
    conn.commit()
    cur.fetchall()

    cur.close()
    conn.close()


def update_received(order_id):
    import pymysql.cursors

    try:
        import pymysql
        pymysql.install_as_MySQLdb()
    except ImportError:
        pass

    conn = pymysql.connect(
     user = "root",
     passwd = "seigo2017",
     host = "localhost",
     db = "vv_db"
    )


    cur = conn.cursor()

    sql = ("UPDATE 【編集禁止】受注テーブル（一覧表示用） SET received = 1 WHERE id = %s")
    cur.execute(sql,order_id)
    conn.commit()
    cur.fetchall()

    cur.close()
    conn.close()


def update_returned(order_id):
    import pymysql.cursors

    try:
        import pymysql
        pymysql.install_as_MySQLdb()
    except ImportError:
        pass

    conn = pymysql.connect(
     user = "root",
     passwd = "seigo2017",
     host = "localhost",
     db = "vv_db"
    )


    cur = conn.cursor()

    sql = ("UPDATE 【編集禁止】受注テーブル（一覧表示用） SET returned = 1 WHERE id = %s")
    cur.execute(sql,order_id)
    conn.commit()
    cur.fetchall()

    cur.close()
    conn.close()


def update_printed(order_id):
    import pymysql.cursors

    try:
        import pymysql
        pymysql.install_as_MySQLdb()
    except ImportError:
        pass

    conn = pymysql.connect(
     user = "root",
     passwd = "seigo2017",
     host = "localhost",
     db = "vv_db"
    )


    cur = conn.cursor()

    sql = ("UPDATE 【編集禁止】受注テーブル（一覧表示用） SET printed = 1 WHERE id = %s")
    cur.execute(sql,order_id)
    conn.commit()
    cur.fetchall()

    cur.close()
    conn.close()

"""def update_flags(order_id,flag):
    import pymysql.cursors

    try:
        import pymysql
        pymysql.install_as_MySQLdb()
    except ImportError:
        pass

    conn = pymysql.connect(
     user = "root",
     passwd = "seigo2017",
     host = "localhost",
     db = "vv_db"
    )


    cur = conn.cursor()

    sql = ("UPDATE 【編集禁止】受注テーブル（一覧表示用） SET %s = 1 WHERE order_id = %s")
    cur.execute(sql,[flag,order_id])
    conn.commit()
    cur.fetchall()

    cur.close()
    conn.close()
"""
