from databasecon import dbconnect

cur = dbconnect()
cm = cur.execute("select categoryid,categoryname from categorymaster")
scum = cur.execute("select subcategoryid,categoryid,subcategoryname from subcategorymaster")
sm = cur.execute("select sector_id,stock_name,stock_code from stockmaster")
records = cur.fetchall()
records1 = cur.fetchall()
records2 = cur.fetchall()
records3 = cur.fetchall()
