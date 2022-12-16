#from Test4 import *
from databasecon import *
import cx_Oracle
from FetchByJoin import *
from StockReader import *
import cx_Oracle
def readall():
    detailsFunction=fetchByJoin() #ICICI Bank Limited-stName, 'Bank'-Subsector Name, 'Finance'-Sector name
    stName=detailsFunction[0]
    subSectorName=detailsFunction[1]
    sectorName=detailsFunction[2]
    stCode=detailsFunction[3] #Stock Code
    capName=fetchCapName(stCode)
    print("The stock code {} has stock name {}, sector name {}, subsector name {} and capname {} ".format(stCode,stName,sectorName,subSectorName,capName))






readall()






