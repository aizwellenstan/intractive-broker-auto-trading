import ib_insync
import datetime

ib = ib_insync.IB()
ib.connect()

futures = [ ib_insync.Future("ES", "CFE", localSymbol=s) for s in ["ESU8","ESZ8"]]
last_lengths = {}

def onBarUpdate(bars, hasNewBar):
    if hasNewBar:
        print("New bar for", bars.contract.localSymbol)

ib.qualifyContracts(*futures)
for f in futures:
    print(f)
    if 0:
        bars = ib.reqHistoricalData(
            f,
            endDateTime='',
            durationStr='900 S',
            barSizeSetting='5 secs',
            whatToShow='bid',
            useRTH=True,
            formatDate=1,
            keepUpToDate=True)
    bars = ib.reqRealTimeBars(f, 5, "TRADES", False)
    last_lengths[f.localSymbol] = 0

ib.barUpdateEvent += onBarUpdate

nLoops = 0
while True:
    ib.waitOnUpdate(1)
    nLoops += 1
    for bars in ib.realtimeBars():
        symbol = bars.contract.localSymbol
        length = len(bars)
        if length > last_lengths[symbol]:
            print(nLoops, datetime.datetime.now(), bars.contract.localSymbol, length, bars[-1])
            last_lengths[symbol] = length

ib.disconnect()
print("Done")