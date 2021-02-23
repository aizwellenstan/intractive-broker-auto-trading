from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

contract = Forex('USDCAD')
#contract = Stock('AMD', 'SMART', 'USD')

order = LimitOrder('BUY', 25000,  1.25)

trade = ib.placeOrder(contract, order)

print(trade)