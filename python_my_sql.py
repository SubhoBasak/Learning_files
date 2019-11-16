# import mysql.connector
#
# mydb = mysql.connector.connect(host = '127.0.0.1',
#                                user = 'root',
#                                password = 'raspberry')
#
# print(mydb)
#
# if mydb:
#     print('Connection successful')
# else:
#     print('Connection error')
#
# import mysql.connector
#
# mydb = mysql.connector.connect(host = '127.0.0.1',
#                                user = 'root',
#                                password = 'raspberry')
#
# cursor = mydb.cursor()
#
# cursor.execute('SHOW databases')
#
# for db in cursor:
#     print(db)
#
# import mysql.connector
#
# mydb = mysql.connector.connect(host = '127.0.0.1',
#                                user = 'root',
#                                password = 'raspberry')
#
# if not mydb:
#     print('Connection error !')
#     exit()
#
# cursor = mydb.cursor()
#
# cursor.execute('USE sql_store')
# cursor.execute('SELECT * FROM customers')
#
# customers = cursor.fetchall()
#
# for customer in customers:
#     print(customer)

