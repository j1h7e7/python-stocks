import requests
import json

auth = open("passwords.txt",'r').readlines()[1].rstrip()
print(auth)

cookies= {
    ".ASPXFORMSAUTH": auth,
}
data = {
    "Quantity": "1",
    "TournamentID": "1",
    "UserName": "j1h7e7",
    "OrderSideID": "1",
    "OrderTypeID": "1",
    "Symbol": "TSLA",
    "Currency": "USD",
    "Exchange": "US"
}
r= requests.post("https://www.wallstreetsurvivor.com/play/tradesecuritiesplace/", data=data, cookies=cookies)