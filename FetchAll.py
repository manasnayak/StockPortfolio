# Add a new menu, which will take input as multiple stock codes(comma separated value) and gives output accordingly
import cx_Oracle, sys
from databasecon import *
from StockPortfolioConst import *


def printStockDetailsBasedOnCode(stockCode):
    try:
        con = cx_Oracle.connect(const.DB_CONNECT)
        cur = con.cursor()
        cur.execute(const.STMST_SELECT)
        records = cur.fetchall()
        # r=inputSt()
        # print(r)
        for column in records:
            if (stockCode == column[0]):
                sm1 = column[0]  # Stock code
                sm2 = column[1]  # Subcategory id
                sm3 = column[2]  # stock name
                dsm = {sm1: (sm2, sm3)}
                # print(dsm)
                stDictVal = dsm.get(sm1)
                subCatId = stDictVal[0]  # Subcategory id
                stName = stDictVal[1]  # Stock name

        cur.execute(const.SUBCAT_SELECT)
        records = cur.fetchall()
        dscm = {}
        for column in records:
            # a = list(column)
            scm1 = column[0]  # subcategory id
            scm2 = column[1]  # category id
            scm3 = column[2]  # subcategory name
            dscm1 = {scm1: (scm2, scm3)}
            dscm.update(dscm1)
        subCatDictVal = dscm.get(subCatId)
        catname = subCatDictVal[0]

        cur.execute(const.CATMST_SELECT)
        records = cur.fetchall()
        dcm = {}
        for column in records:
            # b=list(column)
            cm1 = column[0]  # category id
            cm2 = column[1]  # category name
            dcm1 = {cm1: cm2}
            dcm.update(dcm1)
            catDictVal = dcm.get(catname)  # category name
            # print(g)

        print("The stock code {} has stock name- {}, having subcategory as {} and with Sector as {}".format(stockCode,
                                                                                                            stName,
                                                                                                            subCatDictVal[
                                                                                                                1],
                                                                                                            catDictVal))


    except Exception as e:
        print("We could not find search item please try again")
        print(e)


def mulInput():
    r = input("Enter stock code:").upper()
    return r


def getStockDetails():
    a = mulInput()
    if (len(a) == 1):
        printStockDetailsBasedOnCode(a)
    else:
        # a=getStockDetails(a.split(","))
        s = a.split(",")
        for i in s:
            printStockDetailsBasedOnCode(i)
