#SQL実行文　Fetchallで結果取得
def sql_execute(sql):
    import pymysql.cursors
    #mysqlインポート
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
    #カーソル取得
    cur = conn.cursor(pymysql.cursors.DictCursor)
    #SQL実行
    cur.execute(sql)
    conn.commit()
    result = cur.fetchall()
    conn.commmit()
    cur.close()

    conn.close()
    return result

#データベースと繋げる関数
#Fetchoneの時はこれ
def connect():
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
    return conn
