import csv

def fetchFromCsv():
    try:
        with open(input("Enter the path of the file:"), "r") as fp:
            cr = csv.reader(fp)
            cr.__next__()
            for record in cr:
                stockCode=record[0]


                print(stockCode)
    except FileNotFoundError:
        print("Selected file not found Try again !!!")

fetchFromCsv()