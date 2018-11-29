from iexfinance import Stock
from datetime import datetime

stockname = "GE"
stock = Stock(stockname)

lastprice = 0

while(True):
    curprice = stock.get_price()
    if(curprice != lastprice):
        lastprice = curprice
        print(str(datetime.now().time())+" | "+str(curprice))