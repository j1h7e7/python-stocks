from bot import WSSAPI
import requests
import json

auth = open("passwords.txt",'r').readlines()[1].rstrip()

buyer = WSSAPI(auth)

buyer.buy("TSLA","1")
buyer.sell("TSLA","1")
