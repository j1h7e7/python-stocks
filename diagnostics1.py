from iexfinance import Stock
from iexfinance import get_historical_data
from datetime import datetime


tsla = Stock('AAPL')
print(tsla.get_price())
