import csv, cx_Oracle
from StockPortfolioConst import *
def csvRead():
    try:
        with open(input("Enter the path of the file:"), "r") as fp:
            cr = csv.reader(fp)
            cr.__next__()
            for record in cr:
                print(record)
                stCode = record[1]
                stName = record[2]


                try:
                    con = cx_Oracle.connect(const.DB_CONNECT)
                    cur = con.cursor()
                    cur.execute(const.CSV_INSERT % (stCode, stName))
                    con.commit()
                    print()
                except cx_Oracle.DatabaseError as db:
                    print("Can not insert the data in database", db)


    except FileNotFoundError:
        print("File does not exist")
