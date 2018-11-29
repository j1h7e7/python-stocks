from iexfinance import Stock
from datetime import datetime
from array import *
import time

rawnames = open("stocks.txt",'r').readlines()
stocknames = [n.rstrip() for n in rawnames]

allstocks = {}

#Initialize stocks:
for name in stocknames:
    #print(name)
    allstocks.update({name:Stock(name)})

oldstockvalues = {}
newstockvalues = {}
changes = {}

for name in stocknames:
    #print(stock.get_price())
    oldstockvalues.update({name:allstocks[name].get_price()})

while True:
    time.sleep(5)

    for name in stocknames:
        newstockvalues.update({name:allstocks[name].get_price()})
        changes.update({name:newstockvalues[name]/oldstockvalues[name]-1})
        #changes.update({})
        oldstockvalues.update({name:newstockvalues[name]})

    #sortedchanges = sorted(changes, key=changes.get, reverse=True)

    print(changes)
    #print(sortedchanges)

    for key in changes:
        if changes[key]>0: 
            print("Buy "+key+". It went up "+"{0:.3%}".format(changes[key]))
        if changes[key]<0: 
            print("Short "+key+". It went down "+"{0:.3%}".format(-changes[key]))


