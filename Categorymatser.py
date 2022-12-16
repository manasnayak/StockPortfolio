# program for reading data from oracle
from Databasecur import cm, scum, sm, records1, records2, records3, records
from databasecon import dbconnect
from StockPortfolioConst import *

cur = dbconnect()#Connection to database


def categorymaster():
    cur.execute(const.CATMST_SELECT)
    records = cur.fetchall()
    r = int(input("Enter Number:"))
    for column in records:
        # print(column)
        if (r == column[0]):
            print("Category Id:", column[0])
            print("Category  Name:", column[1])
            break


def subcategorymaster():
    cur.execute(const.SUBCAT_SELECT)
    records = cur.fetchall()
    r = int(input("Enter Number:"))
    for column in records:
        # print(column)
        if (r == column[0]):
            print("Sub Category Id:", column[0])
            print("Category Id:", column[1])
            print("Category  Name:", column[2])
            break


def stocksmaster():
    cur.execute(const.STMST_SELECT)
    records = cur.fetchall()
    r = input("Enter Stock code:").upper()
    for column in records:
        # print(column)
        if (r == column[0]):
            print("Stock code:", column[0])
            print("Stock Name:", column[1])
            print("Subcategory id:", column[2])
            break

    # con.close()

# categorymaster()
# subcategorymaster()
# stocksmaster()
