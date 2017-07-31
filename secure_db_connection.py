#!//usr/bin/python

import cx_Oracle

conn = cx_Oracle.connect ( u'assist_db/assist_db@XE' )

print (conn.version)

curr = conn.cursor()

curr.execute( u'SELECT to_char(1) FROM DUAL' )
rows = curr.fetchall()
for row in rows:
    val = int(row[0])


conn.close()
