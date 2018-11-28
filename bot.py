import requests
import json

class WSSAPI:

    cookies = {}

    def __init__(self,auth):
        #print(auth)

        self.cookies= {
            ".ASPXFORMSAUTH": auth,
        }

    def buy(self, symbol, amount):
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

    def sell(self, symbol, amount):
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