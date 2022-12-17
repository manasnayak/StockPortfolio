from pconst import const

const.DB_CONNECT = "c##babul/soumya@localhost/orcl"
const.STMST_SELECT = "select stock_code,subcategory_id,stock_name from stockmaster"
const.SUBCAT_SELECT = "select subcategoryid,categoryid,subcategoryname from subcategorymaster"
const.CATMST_SELECT = "select categoryid,categoryname from categorymaster"
const.FETCH_SECTORMASTER="select stock_name,stock_code,sector_id from stockmaster where stock_code=('%s')"
const.CSV_INSERT="insert into stockmaster values ('%s','%s')"
const.INSERT_STOCKMASTER="insert into stockmaster (id,stock_code,stock_name) values (%d,'%s','%s')"
const.INSERT_STOCKMARKETCAP="insert into stockmarketcap values (%d,'%s','%s','%s')"
const.SECTORMASTER="select id,name,parentid from sectormaster"
const.MARKETCAP="select capname from marketcapmaster where %d between lower_marketcap and higher_marketcap"
const.GETALL="select s1.name as sector_name, s2.name as subsector_name, s3.name as subsubsector_name, sm.stock_name as stock_name from sectormaster s1 inner join sectormaster s2 on s1.id = s2.parentid inner join sectormaster s3 on  s2.id = s3.parentid inner join stockmaster sm on s3.id = sm.sector_id where stock_code=('%s')"
const.STOCKMARKETCAP="select cap_name from stockmarketcap where stock_code=('%s')"