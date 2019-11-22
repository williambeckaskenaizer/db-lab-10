import mysql.connector

l10db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="megainterface97",
        database="lab10",
        auth_plugin="mysql_native_password"
    )
cursor = l10db.cursor()

insert_vendors = (
            "INSERT INTO vendor"
            "(vendor_id, vendor_name, vendor_acct_payable)"
            "VALUES (%s, %s, %s)"
)
insert_products  = (
            "INSERT INTO product"
            "(product_id, product_name, product_desc, product_price, vendor_id)"
            "VALUES (%s, %s, %s, %s, %s)"
)
insert_orders = (
            "INSERT INTO order_table"
            "(order_id, order_date, order_arrival_date, vendor_id)"
            "VALUES (%s, %s, %s, %s)"
)

insert_line = (
            "INSERT INTO line_item"
            "(order_id, line_number, product_id, line_quantity, line_cost)"
            "VALUES (%s, %s, %s, %s, %s)"
)

# BEGIN Create functions
# TODO: check that entered date is valid
# TODO: update other tables as necessary 

def create_vendor():
    vendor_id = input("Enter vendor id number: ")
    while not check_if_id(vendor_id):
        vendor_id = input("Enter vendor id number: ")
    vendor_name = input("Enter vendor name: ")
    accounts_payable_terms = input("Enter vendor accounts payable: ")

    vendor_values = (vendor_id, vendor_name, accounts_payable_terms)
    cursor.execute(insert_vendors, vendor_values)
        
def create_product():
    product_id = input("Enter product id")
    while not check_if_id(product_id):
        vendor_id = input("Enter product id number: ")
    product_name = input("Enter product name: ")
    product_desc = input("Enter product description: ")
    product_price = input("Enter sale price: ")
    if not product_price.isdecimal():
        print("Price must be of the form 12.34")
    vendor_id = input("Enter product vendor id")

    product_values = (product_id, product_name, product_desc, product_price, vendor_id)
    cursor.execute(insert_products, product_values)
    

def create_order():
    order_id = input("Enter order id")
    while not check_if_id(order_id):
        order_id = input("Enter order id number: ")
    vendor_id = input("Enter order vendor id: ")
    if check_if_id(vendor_id):
        print("Order id must be a number of the form 1111")
    order_date = input("Enter order date (MMDDYYYY): ")
    order_arrival_date = input("Enter order arrival date (MMDDYYYY): ")
    
    order_values = (order_id, order_date, order_arrival_date, vendor_id)
    cursor.execute(insert_orders, order_values)

def create_line():
    order_id = input("Enter order id: ")
    while not check_if_id(order_id):
        order_id = input("Enter vendor id number: ")
    line_number = input("Enter line number: ")
    product_id = input("Enter product id: ")
    while not check_if_id(order_id):
        order_id = input("Enter order id number: ")
    sale_price = input("Enter sale price: ")
    while not check_for_decimal(sale_price):
        sale_price = input("Enter in the form of 12.34")
    order_quantity = input("Enter quantity of product ordered: ")

    line_values = (order_id, line_number, product_id, sale_price, order_quantity)
    cursor.execute(insert_line, line_values)

def check_if_id( entered_id):
    if entered_id.isdigit():
        return True
    else:
        print("please enter an integer.")

def check_for_decimal( value):
    if value.isdecimal():
        return True
    else:
        return False
    
# BEGIN Read functions

def search_table( table, field, keyphrase):
    query =  """SELECT * FROM %s WHERE %s = \"%s\" """ % (table, field, keyphrase)
    
    cursor.execute(query)
    result = cursor.fetchall()
    for thing in result:
        print(thing)

# BEGIN update
def update_table( table, field, new_val, old_val):
    update = """UPDATE %s SET %s = %s WHERE %s = %s """ % (table, field, new_val, field, old_val)
    cursor.execute(update)
    l10db.commit()


def delete_record( rec_type):
    delete_cursor = cursor
    if rec_type == "vendor":
        vendorid = input("Enter vendor id number:")
        # TODO delete products related to vendor
        query = """DELETE FROM vendor WHERE vendor_id = %s""" % (vendorid)
        delete_cursor.execute(query, vendorid)
        l10db.commit()
    if rec_type == "products":
        productid = input("Enter product id number:")
        query = """DELETE FROM product where product_id = %s""" % (productid)
        delete_cursor.execute(query, productid)
        l10db.commit()
    if rec_type == "orders":
        orderid = input("Enter order id number:")
        query = """DELETE FROM order where order_id = %s""" % (orderid)
        delete_cursor.execute(query, orderid)
        l10db.commit()
    if rec_type == "line":
        orderid = input("Enter order id number:")
        linenumber = input("Enter line number, if no line number is entered all lines of order_id will be deleted:")
        if linenumber:
            query = """DELETE FROM line WHERE order_id = %s AND line_number = %s""" % (orderid, linenumber)
            delete_cursor.execute(query, orderid, linenumber)
            l10db.commit()
        elif linenumber is None:
            query = """DELETE FROM line WHERE order_id = %s""" % (orderid)
            delete_cursor.execute(query, orderid)
            l10db.commit()
