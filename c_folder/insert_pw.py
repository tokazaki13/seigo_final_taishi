#編集用インサート
def insert_pw(login_id,new_pw):
    import connect
    import pymysql
    import latest_customer_info
    import insert_customers

    customer_data = latest_customer_info.latest_customer_info(login_id)
    customer_data.insert(0,login_id)
    customer_data.append(new_pw)
    insert_customers.insert_customers(customer_data)



"""
    パスワード以外？（ログインIDも？）の最新顧客情報をセレクトして、customer_dataに入れる 　latest_customer_info(login_id)
    新しいパスワードもcustomer_dataに追加する。 customer_data.append(login_id)とcustomer_data.append(password)
    insert_customers(customer_data)をする。  ★insert_customers.insert_customers(customer_data)
"""
