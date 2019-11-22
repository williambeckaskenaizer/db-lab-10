import xlrd
import datetime
import mysql.connector

workbook = xlrd.open_workbook('/Users/williambeck-askenaizer/Desktop/Mainframe/COMP420/lab10/l10/l10.xlsx')

l10db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="megainterface97",
    database="lab10",
    auth_plugin='mysql_native_password'
)
cursor = l10db.cursor()

add_vendors = (
            "INSERT INTO vendor(vendor_id, vendor_name, vendor_acct_payable) VALUES (%s, %s, %s)"
)

add_products = (
            "INSERT INTO product"
            "(product_id, product_name, product_desc, product_price, vendor_id)"
            "VALUES (%s, %s, %s, %s, %s)"
)

add_orders = (
            "INSERT INTO order_table"
            "(order_id, order_date, order_arrival_date, vendor_id)"
            "VALUES (%s, %s, %s, %s)"
)

add_lines = (
            "INSERT INTO line_item"
            "(order_id, line_number, product_id, line_quantity, line_cost)"
            "VALUES (%s, %s, %s, %s, %s)"
)

xl_sheet = workbook.sheet_by_name("Vendors")
for idx in range(1, xl_sheet.nrows):
    vendor_id = xl_sheet.cell(idx, 0).value
    vendor_name = xl_sheet.cell(idx, 1).value
    accounts_payable_terms = xl_sheet.cell(idx, 2).value

    vendor_values = (vendor_id, vendor_name, accounts_payable_terms)
    cursor.execute(add_vendors, vendor_values)

xl_sheet = workbook.sheet_by_name("Products")
for idx in range(1, xl_sheet.nrows):
    product_id = xl_sheet.cell(idx,0).value
    product_name = xl_sheet.cell(idx, 1).value
    product_desc = xl_sheet.cell(idx, 2).value
    product_price = xl_sheet.cell(idx, 3).value
    vendor_id = xl_sheet.cell(idx, 4).value

    product_values = (product_id, product_name, product_desc, product_price, vendor_id)
    cursor.execute(add_products, product_values)

xl_sheet = workbook.sheet_by_name("Orders")
for idx in range(1, xl_sheet.nrows):
    order_id = xl_sheet.cell(idx, 0).value
    vendor_id = xl_sheet.cell(idx, 1).value
    order_date = xlrd.xldate_as_datetime(xl_sheet.cell(idx, 2).value, workbook.datemode)
    order_arrival_date = xlrd.xldate_as_datetime(xl_sheet.cell(idx, 3).value, workbook.datemode)

    order_values = (order_id, order_date, order_arrival_date, vendor_id)
    cursor.execute(add_orders, order_values)

xl_sheet = workbook.sheet_by_name("Line")
for idx in range(1, xl_sheet.nrows):
    order_id = xl_sheet.cell(idx, 0).value
    line_number = xl_sheet.cell(idx, 1).value
    product_id = xl_sheet.cell(idx, 2).value
    sale_price = xl_sheet.cell(idx, 3).value
    order_quantity = xl_sheet.cell(idx, 4).value

    line_values = (order_id, line_number, product_id, sale_price, order_quantity)
    cursor.execute(add_lines, line_values)
cursor.close()
l10db.commit()
l10db.close()
