from ib_insync import *

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

contract = Stock('AAPL', 'SMART', 'USD')
ib.qualifyContracts(contract)

print(contract)

ib.sleep(1)

chains = ib.reqSecDefOptParams(contract.symbol, '', contract.secType, contract.conId)

print(util.df(chains))