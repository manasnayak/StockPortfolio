from databasecon import *
import csv, cx_Oracle
from StockPortfolioConst import *
def fetchCapName(stCode):
    cur=dbconnect()
    cur.execute(const.STOCKMARKETCAP%stCode)
    record=cur.fetchall()
    print(record)
    return record[0][0]

def marketCapMaster(marketCapAmount):
    try:
        cur = dbconnect()
        cur.execute(const.MARKETCAP%(marketCapAmount))
        records=cur.fetchall()
        for column in records:
            capName = column[0]
            return capName


    except cx_Oracle.DatabaseError as db:
        print("Error in Database",db)
def getSectorAndStockInfo(stockCode):
    cur=dbconnect()
    cur.execute(const.GETALL%stockCode)
    records = cur.fetchall()
    return records[0]