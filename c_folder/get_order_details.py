def get_order_details(cart, order_id):
    order_details = []
    for dict_in in cart:
        details_list = []
        itemcode,name,author,price,discounted,price_tax,num,total,total_tax,item_category,login_id = dict_in.values()

        details_list = [itemcode,name,num,price,price_tax,total,total_tax]
        details_list.insert(0,order_id)
        order_details.append(details_list)
    return order_details
