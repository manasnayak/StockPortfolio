import cx_Oracle
from databasecon import *
from StockReader import *


def fetchByJoin():

    stCode=takeInputFromUser()
    record = getSectorAndStockInfo(stCode)

    sectorName = record[0]
    subSectorName = record[1]
    subSubSectorName=record[2]
    stockName = record[3]



    print("Stock Code:{},Stock Name:{},Subsector Name:{},Sector Name:{},Subsubsector Name:{}".format(stCode, stockName, subSectorName,
                                                                                   sectorName,subSubSectorName))
    return stockName,subSectorName,sectorName,stCode

def takeInputFromUser():
    r = input("Enter Stock Code:").upper()
    return r

