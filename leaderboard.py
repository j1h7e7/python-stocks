import requests
import re
from decimal import Decimal
from re import sub
import numpy
import matplotlib.pyplot as plt

auth = open("passwords.txt",'r').readlines()[1].rstrip()

cookies= {
    ".ASPXFORMSAUTH": auth,
    "WSS.V4": "TournamentID=sYsmtMuuKFnQQEF+JmA/Vw=="
}

r=requests.get("https://www.wallstreetsurvivor.com/league/WolvesofBentley?justjoined=False", cookies=cookies)

#print(r.text)
text = r.text
rawlines = re.findall(r'\$[0-9]{1,3},*[0-9]{3}\.[0-9]{2}</td>\r\n *</tr>', text)
lines = [rawlines[n] for n in range(0,int((len(rawlines)-1)/3))]

amount = []

for line in lines:
    amount.append([float(Decimal(sub(r'[^\d.]', '', line)))])

print("Mean: "+str(numpy.mean(amount)))
print("Median: "+str(numpy.median(amount)))
print("Std. Dev: "+str(numpy.std(amount)))

a = numpy.hstack(amount)
#plt.hist(a, bins=16)
#plt.show()