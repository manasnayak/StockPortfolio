from databasecon import *
import csv, cx_Oracle
from StockPortfolioConst import *
def fetchCapName(stCode):
    cur=dbconnect()
    cur.execute("select cap_name from stockmarketcap where stock_code=('%s')"%stCode)
    record=cur.fetchall()
    return record[0][0]

def marketCapMaster(marketCapAmount):
    try:
        cur = dbconnect()
        cur.execute("select capname from marketcapmaster where %d between lower_marketcap and higher_marketcap"%(marketCapAmount))
        records=cur.fetchall()
        for column in records:
            capName = column[0]
            return capName


    except cx_Oracle.DatabaseError as db:
        print("Error in Database",db)
def getSectorAndStockInfo(stockCode):
    cur=dbconnect()
    cur.execute("select s1.name as sector_name,s2.name as subsector_name,s1.id as parent_id,s2.id as id,sm.stock_code as code,sm.stock_name as stock_name from sectormaster s1 inner join sectormaster s2 on s1.id=s2.parentid inner join stockmaster sm on s2.id = sm.subcategory_id where stock_code=('%s')"%stockCode)
    records = cur.fetchall()
    print(records)
    return records[0]

#THANKS
#Welcome