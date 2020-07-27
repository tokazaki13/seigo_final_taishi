
"""
tabulate.WIDE_CHARS_MODE = False
"""



def item_info(data,column):
    import pandas
    from pandas import DataFrame
    import unicodedata
    from tabulate import tabulate

    df = pandas.DataFrame(data=data, columns=column)
    result = tabulate(df, df.columns,tablefmt = "github",showindex=False)
    print(result)

"""item_info([[1,"あ","あいう"]],["受注ID","商品名","商品詳細"])
"""
