from ib_insync import *
import time
"""
starttime = time.time()
while True:
    print("tick")
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))
"""
ib = IB()

# IB Gateway
# ib.connect('127.0.0.1', 4002, clientId=1)

# TWS
ib.connect('127.0.0.1', 7497, clientId=1)

contract = Forex('USDCAD')
# contract = Stock('AMD', 'SMART', 'USD')

"""timeframes
1 secs, 5 secs, 10 secs, 15 secs, 30 secs, 1 min, 2 mins, 3 mins, 5 mins, 10 mins, 15 mins, 20 mins, 30 mins, 1 hour, 2 hours, 3 hours, 4 hours, 8 hours, 1 day, 1W, 1M
"""
bars = ib.reqHistoricalData(
        contract, endDateTime='', durationStr='30 D',
        barSizeSetting='1 day', whatToShow='ASK', useRTH=True)
bars=bars[::-1]

df = util.df(bars)
print(df)

close1=bars[1].close
close2=bars[2].close
close3=bars[3].close

print(close1)
print(close2)
print(close3)

hour = ib.reqCurrentTime().hour
minute = ib.reqCurrentTime().minute
print(hour)
print(minute)
#######################