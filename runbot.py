from bot import WSSAPI
from iexfinance import Stock
import requests
import json

auth = open("passwords.txt",'r').readlines()[1].rstrip()

stockname = "GE"
user = WSSAPI(auth)
stock = Stock(stockname)

initialbal = user.checkbalance()
price1 = stock.get_price()
user.buy(stockname,"1")
price2 = stock.get_price()
finalbal = user.checkbalance()

print()
print("Price1: "+str(price1))
print("Price2: "+str(price2))
print("Website Price: "+str(initialbal-finalbal-10))
