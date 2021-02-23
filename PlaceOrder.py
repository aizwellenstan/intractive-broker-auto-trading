from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

contract = Forex('USDCAD')
#contract = Stock('AMD', 'SMART', 'USD')

# order = LimitOrder('SELL', 25000,  1.258)
order = MarketOrder('SELL', 25000)

trade = ib.placeOrder(contract, order)

print(trade)

def orderFilled(trade, fill):
    print("order filled")
    print(order)
    print(fill)

trade.fillEvent += orderFilled

ib.run()