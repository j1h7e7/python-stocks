import requests
import json

class WSSAPI:
    cookieslst=[".ASPXFORMSAUTH" ,"WSS.V4", "WSSOverlay", "_ASPNETSSOWSS","_ga","_gid","incap_ses_258_371548", "visid_incap_1560758","visid_incap_371548"]
    username ="km_ni"
    tID=""
    cookies = {}
    cookieName = "cookiesBentley.json"

    def __init__(self, tournamentID=1):
        self.tID = str(tournamentID)

        with open(self.cookieName) as jsonfile:
            cookieReader = json.load(jsonfile)
            for cookie in cookieReader:
                if cookie["name"] in self.cookieslst:
                    self.cookies[cookie["name"]] = cookie["value"]
                if cookie["name"] == self.username:
                    self.username = cookie["value"]
                    
        
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
            "TournamentID": self.tID,
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
        print(r)
    
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
            "TournamentID": self.tID,
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