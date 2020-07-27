
def VV_batch2():

    import sys
    sys.path.append("/Users/User/Documents/seigo_final/customers/c_folder")
    import connect
    import pymysql
    import datetime
    from dateutil.relativedelta import relativedelta
    import item_info
    import pandas
    from pandas import DataFrame
    import unicodedata
    from tabulate import tabulate

    conn = connect.connect()

    cur = conn.cursor(pymysql.cursors.DictCursor)

    today = datetime.date.today()
    one_month_ago = today - relativedelta(months=1)
    one_month_ago = one_month_ago.month

    sql = ("select 表示用受注テーブル.受注日, 表示用受注明細テーブル.受注ID, 表示用受注明細テーブル.商品コード, 商品情報一覧テーブル.商品名, 表示用受注明細テーブル.数量, 表示用受注明細テーブル.税抜小計, (表示用受注明細テーブル.税込小計 - 表示用受注明細テーブル.税抜小計) as '税額', 表示用受注テーブル.配送料 as '送料', CAST((表示用受注テーブル.配送料/1.1) as signed) as '送料税額' \
    from 商品情報一覧テーブル inner join 表示用受注明細テーブル on 商品情報一覧テーブル.商品コード = 表示用受注明細テーブル.商品コード left outer join 表示用受注テーブル on 表示用受注明細テーブル.受注ID = 表示用受注テーブル.受注ID\
    order by 表示用受注明細テーブル.受注ID asc")

    cur.execute(sql)

    conn.commit()
    result = cur.fetchall()
    cur.close()
    conn.close()


    list = []
    column = ["日付","明細ID","商品ID","商品名","個数","金額","税額","送料","送料税額"]
    price_list = []
    tax_list = []
    fee_result = 0
    fee_tax_result = 0
    id_list = []
    date_list = []
    for batch_1 in result:
        list_count = len(list) - 1
        order_date,order_id,itemcode,i_name,ordernum,price,tax,fee,fee_tax = batch_1.values()

        price = int(price)
        tax = int(tax)
        order_date_month = order_date.month


        if order_date_month == one_month_ago:
            if order_id not in id_list:
                order_date = order_date.strftime('%Y/%m/%d')

                if order_date not in date_list:
                    batch_list = [order_date,order_id,itemcode,i_name,ordernum,price,tax,fee,fee_tax]
                    list.append(batch_list)
                    price_list.append(price)
                    tax_list.append(tax)
                    fee_result += fee
                    fee_tax_result += fee_tax
                    id_list.append(order_id)
                    date_list.append(order_date)
                else:
                    batch_list = ["",order_id,itemcode,i_name,ordernum,price,tax,fee,fee_tax]
                    list.append(batch_list)
                    price_list.append(price)
                    tax_list.append(tax)
                    fee_result += fee
                    fee_tax_result += fee_tax
                    id_list.append(order_id)
            else:
                batch_list = ["","",itemcode,i_name,ordernum,price,tax,"",""]
                list.append(batch_list)
                price_list.append(price)
                tax_list.append(tax)




    p_sum = sum(price_list)
    t_sum = sum(tax_list)
    batch_list = ["","","","","","","","",""]
    list.append(batch_list)
    batch_list = ["","","","","商品合計",p_sum,t_sum,fee_result,fee_tax_result]
    list.append(batch_list)




    """
    昇順で並んでいるので、商品コードが被ったら、前の情報に数量をプラス
    batch_listでくくる前に被り☑を入れて、被りなら前のbatch_listの数量とSUM
    """
    title = "【"+str(one_month_ago)+"月分月次売上明細】\n\n"

    df = pandas.DataFrame(data=list, columns=column)
    result = tabulate(df, df.columns,tablefmt = "github",showindex=False)
    #item_info.item_info(list,column)
    out = title + result
    filename = str(one_month_ago)+"月分月次売上明細.txt"
    f = open("C:\\Users\\User\\Documents\\seigo_final\\VVstore\\output\\月次売上明細\\"+filename, 'w')

    f.write(out)
    f.close()
VV_batch2()


"""
＊月次売上明細
日付、明細ID、商品ID、商品名、数量、金額、税額（税込ー税抜）、送料、送料税額
"""
