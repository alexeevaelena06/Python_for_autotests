from Model.group import Group
# import random
# import string


testdata = [Group(group_name="name1", group_header="header1", group_footer="footer1"),
            Group(group_name="name2", group_header="header2", group_footer="footer2")
            ]


# def random_string(prefix, maxlen):
#     symbols = string.ascii_letters+string.digits+string.punctuation+" "*10
#     return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])
#
#
# testdata = [Group(group_name=group_name, group_header=group_header,
#                   group_footer=group_footer)
#             for group_name in ["", random_string("name", 10)]
#             for group_header in ["", random_string("header", 20)]
#             for group_footer in ["", random_string("footer", 20)]
#             ]
