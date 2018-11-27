from alpha_vantage.timeseries import TimeSeries
from pprint import pprint

def comparetimes(i, f, timesData):
    if(timesData[f][3]>=timesData[i][2]):
        return True
    return False

def printtimes(i, f, timesData):
    print("At "+timesData[i][0]+" the max price was: "+str(timesData[i][2]))
    print("At "+timesData[f][0]+" the min price was: "+str(timesData[f][3]))
    print()

key = open("passwords.txt",'r').readline().rstrip()

ts = TimeSeries(key=key, output_format='csv')
data, meta_data = ts.get_intraday(symbol='GOOG',interval='1min')
timesData=[row for row in data]
for i in range(2,16):
    for j in range(1,i):
        if(comparetimes(i,j,timesData)):
            printtimes(i,j,timesData)