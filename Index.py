from FetchAll import *
from menu import menu
from InsertRecord import *
from StockDetailsCsvRead import *
from SectorMasterFetch import *
from Categorymatser import categorymaster, subcategorymaster, stocksmaster
from FetchByJoin import  *
import sys

menu()

while (True):
    try:
        print("-" * 50)
        ch = int(input("Enter your choice:"))
        if (ch <= 0 or ch > 11):
            print("Please Enter a number between 1 to 11")
        else:
            print("-" * 50)
            match (ch):
                case 1:
                    categorymaster()
                case 2:
                    subcategorymaster()
                case 3:
                    stocksmaster()
                case 4:
                    getStockDetails()
                case 5:
                    insertRecord()
                case 6:
                    updateRecord()
                case 7:
                    deleteRecord()
                    #Above all for practice purpose
                case 8:
                    csvRead()
                case 9:
                    sectorMasterFetch()
                case 10:
                    fetchByJoin()
                case 11:
                    con = input("Do you want to EXIT (yes/no):").lower()
                    print("-" * 50)
                    if (con == "yes"):
                        print("Thanks for using this program")
                        sys.exit()
    except ValueError as v:
        print("Please enter number 1 to 11. Don't Enter strs/symbols/alnums")
        print(v)
