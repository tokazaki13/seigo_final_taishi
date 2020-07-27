def VV3():
    import sys
    sys.path.append("/Users/User/Documents/seigo_final/customers/c_folder")
    import VV_show_orders
    import update_flags

    import VV0_start_menu
    import yes_no


    print("\n～～～～～～～～～～～～～～～～～～\n\n【入金済み登録】")

    result, order_id = VV_show_orders.VV_show_orders()
    if result is False:
        VV0_start_menu.VV0()
    """フラグUPDATE"""

    update_flags.update_received(order_id)

    print("\n★引き続き、入金済み登録を行いますか★\n")
    num = yes_no.yes_no_only()
    if num == 1:
        VV3()
    VV0_start_menu.VV0()
