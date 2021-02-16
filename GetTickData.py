from ib_insync import *

ib = IB()

# IB Gateway
# ib.connect('127.0.0.1', 4002, clientId=1)

# TWS
ib.connect('127.0.0.1', 7497, clientId=1)

# contract = Forex('EURUSD')
contract = Stock('AMD', 'SMART', 'USD')

market_data = ib.reqMktData(contract, '', False, False)

def onPendingTicker(ticker):
    print(ticker)

ib.pendingTickersEvent += onPendingTicker

ib.run()
