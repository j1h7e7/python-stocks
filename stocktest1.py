from alpha_vantage.timeseries import TimeSeries
from pprint import pprint
from array import *

def comparetimes(i, f, timesData):
    if(timesData[f][3]>=timesData[i][2]):
        return True
    return False

def printtimes(i, f, timesData):
    print("At "+timesData[i][0]+" the max price was: "+str(timesData[i][2]))
    print("At "+timesData[f][0]+" the min price was: "+str(timesData[f][3]))
    profit = float(timesData[f][3])/float(timesData[i][2])-1
    print("That gives a profit of "+"{0:.3%}".format(profit))
    #print("That means a profit of "+"{0:.3%}".format(profit/(i-f))+" per minute")
    print()

key = open("passwords.txt",'r').readline().rstrip()

ts = TimeSeries(key=key, output_format='csv')
data, meta_data = ts.get_intraday(symbol='TSLA',interval='1min')
timesData=[row for row in data]

profitTimes = []

for i in range(2,16):
    for f in range(1,i):
        if(comparetimes(i,f,timesData)):
            printtimes(i,f,timesData)
            profitTimes.append([i,f,(float(timesData[f][3])/float(timesData[i][2])-1)])

def profit(e):
    return e[2]

profitTimes.sort(reverse=True, key=profit)

print("The highest profit in that time was:")
printtimes(profitTimes[0][0],profitTimes[0][1],timesData)