# import pymysql.cursors
# from Fixture.db import DbFixture
from Fixture.orm import ORMFixture

# connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
# db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
from Model.group import Group

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

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
    l = db.get_contacts_not_in_group(Group(id='152'))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()
