#!/usr/bin/env python

import re, pg, os, MySQLdb

db = MySQLdb.connect(host="localhost", user="root", passwd="dfc1!!", db="rackmonkey")

cursor = db.cursor()
cursor.execute(""" select id, name, custom_info from device """)
result = cursor.fetchall()
for rr in result:
    item = ''
    for r in rr:
	item = item + str(r) + '\t'
    print item

db.close()

