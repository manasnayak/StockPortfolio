import cx_Oracle
def dbconnect():
    con=cx_Oracle.connect("c##babul/soumya@localhost/orcl")
    cur=con.cursor()
    cur.execute("select st.name,st.code,s.subcategoryname,s.subcategoryid from stocksmaster st,subcategorymaster s where st.subcategory=s.subcategoryid")
    records1=cur.fetchall()
    r=input("Enter Stock Code:").upper()
    for c in records1:
        if (r==c[1]):
            stname=c[0]
            stCode=c[1]
            subCategoryName=c[2]
            subCategoryid=c[3]

            #Thank you


    #Thank you for this program
    #Welcome

    cur.execute("select c.categoryname,s.subcategoryname,s.subcategoryid from categorymaster c,subcategorymaster s where c.categoryid=s.categoryid")
    records = cur.fetchall()
    for column in records:
        if (subCategoryid==column[2]):
            categoryName=column[0]


    print("Stock Code:{},Stock Name:{},SubcategoryName:{},Category Name:{}".format(stCode,stname,subCategoryName,categoryName))






dbconnect()