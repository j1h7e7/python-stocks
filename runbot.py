from bot import WSSAPI
from iexfinance import Stock
import requests
import json
import time

auth = open("passwords.txt",'r').readlines()[1].rstrip()

stockname = "GE"
user = WSSAPI(auth)
stock = Stock(stockname)

initialbal = user.checkbalance()
price1 = stock.get_price()
user.buy(stockname,"10")
price2 = stock.get_price()
loop = True
while(loop):
    finalbal = user.checkbalance()
    if finalbal < initialbal:
        loop = False

print()
print("Price1: "+str(price1))
print("Price2: "+str(price2))
print("Website Price: "+str((initialbal-finalbal-10)/10))
