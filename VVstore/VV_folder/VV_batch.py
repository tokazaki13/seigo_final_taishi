def VV_batch():

    import sys
    sys.path.append("/Users/User/Documents/seigo_final/customers/c_folder")
    import connect
    import pymysql
    from datetime import datetime
    from dateutil.relativedelta import relativedelta
    import item_info
    import pandas
    from pandas import DataFrame
    import unicodedata
    from tabulate import tabulate

    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)

    today = datetime.today()
    one_month_ago = today - relativedelta(months=1)
    one_month_ago = one_month_ago.month

    sql = ("select 商品情報一覧テーブル.商品コード, 商品情報一覧テーブル.商品名, 商品情報一覧テーブル.取扱状況, 表示用受注明細テーブル.数量, 表示用受注明細テーブル.税抜小計, 表示用受注テーブル.受注日 \
    from 商品情報一覧テーブル left outer join 表示用受注明細テーブル on 商品情報一覧テーブル.商品コード = 表示用受注明細テーブル.商品コード left outer join 表示用受注テーブル on 表示用受注明細テーブル.受注ID = 表示用受注テーブル.受注ID \
    order by 商品情報一覧テーブル.商品コード asc")

    cur.execute(sql)

    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()


    column = ["商品ID","商品名","商品取扱状況","売上合計個数","売上合計金額（税抜）"]
    list = []
    itemcode_list = []
    sum_l = []
    for batch_1 in result:
        list_count = len(list) - 1
        itemcode, i_name, current_status, ordernum, total_with_tax, order_date = batch_1.values()

        if current_status == 0:
            current_status = "取扱中"
        elif current_status == 1:
            current_status = "販売停止中"
        if ordernum is None:
            ordernum = 0
            total_with_tax = "0"
        total_with_tax = int(total_with_tax)
        if order_date is not None:
            order_date = order_date.month

        if order_date == one_month_ago:
            if itemcode not in itemcode_list:
                batch_list = [itemcode, i_name, current_status, ordernum, total_with_tax]
                itemcode_list.append(itemcode)
                list.append(batch_list)
            else:
                latest = list[list_count]
                latest[3] += ordernum
                latest[4] += total_with_tax
        else:
            ordernum = 0
            total_with_tax = 0
            if itemcode not in itemcode_list:
                batch_list = [itemcode, i_name, current_status, ordernum, total_with_tax]
                itemcode_list.append(itemcode)
                list.append(batch_list)

    for l in list:
        a = l[4]
        sum_l.append(a)
    sum_total = sum(sum_l)
    batch_list = ["","","","総合計金額",sum_total]
    list.append(batch_list)




    """
    昇順で並んでいるので、商品コードが被ったら、前の情報に数量をプラス
    batch_listでくくる前に被り☑を入れて、被りなら前のbatch_listの数量とSUM
    """
    title = "【"+str(one_month_ago)+"月分商品別売上集計】\n\n"

    df = pandas.DataFrame(data=list, columns=column)
    result = tabulate(df, df.columns,tablefmt = "github",showindex=False)
    #item_info.item_info(list,column)
    out = title + result
    filename = str(one_month_ago)+"月分商品別売上集計.txt"
    f = open("C:\\Users\\User\\Documents\\seigo_final\\VVstore\\output\\月次商品別売上\\"+filename, 'w')

    f.write(out)
    f.close()

VV_batch()
"""
＊月次商品別売上合計
商品コード、商品名、削除フラグ（販売中、販売停止中）、売上合計個数、売上合計金額（税抜き）

商品情報一覧テーブルと売上明細テーブル結合（商品コードで）
受注テーブルと結合＆受注日のみ取得
商品コード昇順


＊月次売上明細
日付、明細ID、商品ID、商品名、数量、金額、税額（税込ー税抜）、送料、送料税額
"""
#coding: utf-8
