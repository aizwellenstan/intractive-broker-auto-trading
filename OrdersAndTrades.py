from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

for trade in ib.trades():
    print("========trade==========")
    print(trade)
    
"""
for order in ib.orders():
    print("========order==========")
    print(order)
"""

ib.run()