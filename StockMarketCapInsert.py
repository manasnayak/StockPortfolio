import csv, cx_Oracle
from StockPortfolioConst import *
from StockReader import *




def readCsvInsert():
    try:
        with open(input("Enter the path of the file:"), "r") as fp:
            cr = csv.reader(fp)
            cr.__next__()
            for record in cr:
                id=int(record[0])
                stCode = record[1]
                stName = record[2]
                marketCap=int(record[3])


                try:
                    con = cx_Oracle.connect(const.DB_CONNECT)
                    cur = con.cursor()
                    cur.execute(const.INSERT_STOCKMASTER % (id,stCode, stName))

                    capName= marketCapMaster(marketCap)

                    cur.execute(const.INSERT_STOCKMARKETCAP %(id, stCode, marketCap,capName))
                    con.commit()

                    print()



                except cx_Oracle.DatabaseError as db:
                    print("Can not insert the data in database", db)

    except FileNotFoundError:
        print("File does not exist")



readCsvInsert()