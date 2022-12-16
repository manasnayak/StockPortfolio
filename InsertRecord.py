import cx_Oracle, sys
from StockPortfolioConst import *
from databasecon import *


def insertRecord():
    while (True):
        try:
            con = cx_Oracle.connect(const.DB_CONNECT)
            cur = con.cursor()
            sName = input("Enter Stock Name:")
            sCode = input("Enter Stock Code:").upper()
            subId = int(input("Enter SubCategory Id:"))
            cur.execute("insert into stocksmaster values ('%s','%s',%d)" % (sName, sCode, subId))
            con.commit()
            print("{} stock record inserted successfully".format(cur.rowcount))
            ch = input("Do u want to insert another record (yes/no):")
            if (ch.lower() == "no"):
                sys.exit()
        except cx_Oracle.DatabaseError as db:
            print("Problem in Database")


def updateRecord():
    while (True):
        try:
            con = cx_Oracle.connect(const.DB_CONNECT)
            cur = con.cursor()
            sName = input("Enter Stock Name for update:")
            sCode = input("Enter Stock Code for update:").upper()
            subId = int(input("Enter SubCategory Id for update:"))
            cur.execute("update stocksmaster set NAME='%s',SUBCATEGORY=%d where CODE='%s'" % (sName, subId, sCode))
            con.commit()
            if (cur.rowcount > 0):
                print("{} stock record updated successfully".format(cur.rowcount))
            else:
                print("Record does not exist")
            ch = input("Do u want to insert another record (yes/no):")
            if (ch.lower() == "no"):
                sys.exit()
        except cx_Oracle.DatabaseError as db:
            print("Problem in Database")


def deleteRecord():
    while (True):
        try:
            con = cx_Oracle.connect(const.DB_CONNECT)
            cur = con.cursor()
            sCode = input("Enter Stock Code for delete:").upper()
            cur.execute("delete from stocksmaster where CODE='%s'" % (sCode))
            con.commit()
            if (cur.rowcount > 0):
                print("{} stock record deleted successfully".format(cur.rowcount))
            else:
                print("Record does not exist")
            print("{} stock record inserted successfully".format(cur.rowcount))
            ch = input("Do u want to insert another record (yes/no):")
            if (ch.lower() == "no"):
                sys.exit()
        except cx_Oracle.DatabaseError as db:
            print("Problem in Database")
