def out_bill(data,column,billing_amount,shipping_fee,billdate,bill_info,customer_name,sum_total,sum_total_tax,sum_tax):
    import pandas
    from pandas import DataFrame
    import unicodedata
    from tabulate import tabulate
    import datetime
    """
    tabulate.WIDE_CHARS_MODE = False
    """



    df = pandas.DataFrame(data=data, columns=column)
    result = tabulate(df, df.columns,tablefmt = "github",showindex=False)

    a = "【請求書】\n請求日："+billdate[0].strftime('%Y年%m月%d日')+"\n入金期限："+billdate[1].strftime('%Y年%m月%d日')
    line = "\n-----------------------------------------\n"
    b = "【請求先】\n名前："+bill_info[0]+"\n郵便番号："+bill_info[1]+"\n住所："+bill_info[2]+"\n電話番号："+bill_info[3]+"\nメールアドレス："+bill_info[4]
    c = "【請求情報】\n\n\n" + result
    d = "\n\n配送料：" + str(shipping_fee)
    g = "\n税抜合計額：" + str(sum_total) +"円"
    h = "\n税額合計：" + str(sum_tax) + "円"
    e = "\n税込合計額：" + str(billing_amount) +"円"
    j = "【振込先口座情報】\n"
    i = "【お問い合わせ先】\n"
    k = "住所：東京都赤坂２－１４－３２ 赤坂２・１４プラザビル　4階"
    l = "\n電話番号：03-3560-4061"
    m = "\nメールアドレス：atsushi.kato@ctp.co.jp"
    n = "\nご利用ありがとうございました。"
    o = "　・ゆうちょ銀行\n　・店番：１９８\n　・店名：一九八店\n　・口座番号：1234567\n"

    z = a + line + b + line + c + d + g + h + e + line + j + o + line + i + k + l + m + n

    now = datetime.datetime.now()
    filename = customer_name + "＿" + now.strftime('%Y%m%d_%H%M%S') + '.txt'
    f = open("C:\\Users\\User\\Documents\\seigo_final\\customers\\output\\"+filename, 'w')
    f.write(z)
    f = open("C:\\Users\\User\\Documents\\seigo_final\\VVstore\\output\\unsent\\"+filename, 'w')
    f.write(z)
    f.close()
    print(filename + "が出力されました")
