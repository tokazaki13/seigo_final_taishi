def VV1():
    import sys
    sys.path.append("/Users/User/Documents/seigo_final/customers/c_folder")
    import show_for_deliver
    import get_bill
    import out_for_deliver
    import VV0_start_menu
    import yes_no
    import update_flags

    print("\n～～～～～～～～～～～～～～～～～～\n\n【明細書出力】")


    result, order_id = show_for_deliver.show_for_deliver()
    if result is False:
        VV0_start_menu.VV0()

    billing_amount,shipping_fee,order_details,billdate,bill_info,customer_name,sum_total,sum_total_tax,sum_tax = get_bill.get_bill(order_id)
    column = ["商品番号","商品名","商品詳細","税込単価","（税抜単価）","税率","数量","税込小計","（税抜小計）"]

    out_for_deliver.out_bill(order_details,column,billing_amount,shipping_fee,billdate,bill_info,customer_name,sum_total,sum_total_tax,sum_tax)


    update_flags.update_printed(order_id)

    print("\n★引き続き、出庫用明細書出力を行いますか★\n")
    num = yes_no.yes_no_only()
    if num == 1:
        VV1()
    VV0_start_menu.VV0()
