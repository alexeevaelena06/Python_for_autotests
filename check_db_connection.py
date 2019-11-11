# import pymysql.cursors
from Fixture.db import DbFixture

# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

# try:
#     cursor = connection.cursor()
#     cursor.execute("select * from group_list")
#     for row in cursor.fetchall():
#         print(row)
# finally:
#     connection.close()

# try:
#     groups = db.get_group_list()
#     for group in groups:
#         print(group)
#     print(len(groups))
# finally:
#     db.destroy()

try:
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print(len(contacts))
finally:
    db.destroy()
