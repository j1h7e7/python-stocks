import requests
import re
from re import sub
from decimal import Decimal

class BalCheck:

    cookies={}

    def __init__(self,auth):
        #print(auth)

        self.cookies= {
            ".ASPXFORMSAUTH": auth,
            #"WSS.V4": "TournamentID=sYsmtMuuKFnQQEF+JmA/Vw=="
        }

    def checkbalance(self):

        r=requests.get("https://www.wallstreetsurvivor.com/accountoverview", cookies=self.cookies)
        text = r.text
        line = re.search('<li class="select" data-tabinfo="a">.*', text).group(0)
        amount = re.search('\$[0-9]{0,3},*[0-9]{1,3}\.[0-9]{2}', line).group(0)
        value = Decimal(sub(r'[^\d.]', '', amount))
        #print(value)
        return value


auth = open("passwords.txt",'r').readlines()[1].rstrip()

bal = BalCheck(auth)

print(bal.checkbalance())