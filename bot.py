import requests
import json

class WSSAPI:
    cookieslst=[".ASPXFORMSAUTH" ,"WSS.V4", "WSSOverlay", "_ASPNETSSOWSS","_ga","_gid","incap_ses_258_371548", "visid_incap_1560758","visid_incap_371548"]
    username =""
    cookies = {}
    cookieName = "cookies.json"

    def __init__(self, username):
        self.username = username

        with open(self.cookieName) as jsonfile:
            cookieReader = json.load(jsonfile)
            for cookie in cookieReader:
                if cookie["name"] in self.cookieslst:
                    self.cookies[cookie["name"]] = cookie["value"]
        
    def buy(self, ticker, number):
        dataBuy = {
            "IncludeHtml": "false",
            "SecurityID": "3789",
            "SecurityTypeID": "1",
            "Quantity": str(number),
            "PriceBought": "0",
            "QuantityOwned": "0",
            "WorstPerformingSecurityID": "0",
            "StockRecommended": "False",
            "CallPutIndicator": "",
            "LimitStopPrice": "",
            "ExpirationDate": "",
            "Expiration": "0",
            "DateToExpire": "",
            "StrikePrice": "",
            "TournamentID": "1",
            "UserName": self.username,
            "OrderSideID": "1",
            "OrderTypeID": "1",
            "Symbol": ticker,
            "CompanyName": "Tesla+Inc",
            "ActionName": "",
            "ActionValue": "0",
            "IsLastStep": "False",
            "Currency": "USD",
            "MaxShares": "137",
            "EditOrder": "False",
            "CancelOrderID": "-1",
            "trade": "",
            "edit": "",
            "Exchange": "US"
        }
        r = requests.post("https://www.wallstreetsurvivor.com/play/tradesecuritiesplace/", data=dataBuy, cookies=self.cookies)
    
    def sell(self, ticker, number):
        dataSell ={
            "IncludeHtml": "false",
            "SecurityID": "3789",
            "SecurityTypeID": "1",
            "Quantity": str(number),
            "PriceBought": "0",
            "QuantityOwned": "0",
            "WorstPerformingSecurityID": "0",
            "StockRecommended": "False",
            "CallPutIndicator": "",
            "LimitStopPrice": "",
            "ExpirationDate": "",
            "Expiration": "0",
            "DateToExpire": "",
            "StrikePrice": "",
            "TournamentID": "1",
            "UserName": self.username, 
            "OrderSideID": "2",
            "OrderTypeID": "1",
            "Symbol": ticker,
            "CompanyName": "Apple Inc",
            "ActionName": "",
            "ActionValue": "0",
            "IsLastStep": "False",
            "Currency": "USD",
            "MaxShares": "4",
            "EditOrder": "False",
            "CancelOrderID": "-1",
            "trade": "",
            "edit": "",
            "Exchange": "US",
        }
        r=requests.post("https://www.wallstreetsurvivor.com/play/tradesecuritiesplace/", data=dataSell, cookies=self.cookies)