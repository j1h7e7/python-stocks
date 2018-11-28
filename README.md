# Python Stocks
This is an unofficial python API for https://www.wallstreetsurvivor.com/accountoverview/. To use it you must get this chrome extension https://chrome.google.com/webstore/detail/editthiscookie/fngmhnnpilhplaeedifhccceomclgfbg?hl=en. With that extension, you can copy all of your cookies on the Wall Street survivor buy page. Then paste them into a cookies.json file in the directory of bot.py.

Then make an instance of WSSAPI with the tournament id (default is one for the practice portfolio). After this, you can use a function to buy, sell and trade stocks on your account.

## Examples
```python
from bot import WSSAPI
w = wssAPI(1)
w.buy("TSLA",1)
w.sell("TSLA",1)
```

## Commands
WSSAPI.buy(String of the stock ticker, number of stocks)

WSSAPI.sell(String of the stock ticker, number of stocks)