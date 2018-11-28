import requests
import json
import requests
import re
from re import sub
from decimal import Decimal

class WSSAPI:

    cookies = {}

    def __init__(self,auth):
        #print(auth)
        self.cookies= {
            ".ASPXFORMSAUTH": auth,
            #"WSS.V4": TID
        }

    def buy(self, symbol, amount):
        print("Buying "+amount+" of "+symbol)

        data = {
            "Quantity": amount,
            "TournamentID": "1",
            "UserName": "j1h7e7",
            "OrderSideID": "1",
            "OrderTypeID": "1",
            "Symbol": symbol,
            "Currency": "USD",
            "Exchange": "US"
        }
        r= requests.post("https://www.wallstreetsurvivor.com/play/tradesecuritiesplace/", data=data, cookies=self.cookies)

        print("Bought")

    def sell(self, symbol, amount):
        print("Selling "+amount+" of "+symbol)

        data = {
            "Quantity": amount,
            "TournamentID": "1",
            "UserName": "j1h7e7",
            "OrderSideID": "2",
            "OrderTypeID": "1",
            "Symbol": symbol,
            "Currency": "USD",
            "Exchange": "US"
        }
        r= requests.post("https://www.wallstreetsurvivor.com/play/tradesecuritiesplace/", data=data, cookies=self.cookies)

        print("Sold")

    def checkbalance(self):
        print("Checking balance")

        r=requests.get("https://www.wallstreetsurvivor.com/accountoverview", cookies=self.cookies)
        text = r.text
        line = re.search('<li class="select" data-tabinfo="a">.*', text).group(0)
        amount = re.search('\$[0-9]{0,3},*[0-9]{1,3}\.[0-9]{2}', line).group(0)
        value = Decimal(sub(r'[^\d.]', '', amount))
        print("Balance: "+amount)
        return value