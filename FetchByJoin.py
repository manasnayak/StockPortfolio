import cx_Oracle
from databasecon import *
from StockReader import *


def fetchByJoin():

    stCode=takeInputFromUser()
    record = getSectorAndStockInfo(stCode)
    sectorName = record[0]
    subSectorName = record[1]
    parentId=record[2]
    id = record[3]
    stockCode=record[4]
    stockName=record[5]


    print("Stock Code:{},Stock Name:{},Subsector Name:{},Sector Name:{}".format(stockCode, stockName, subSectorName,
                                                                                   sectorName))
    return stockName,subSectorName,sectorName,stockCode

def takeInputFromUser():
    r = input("Enter Stock Code:").upper()
    return r

