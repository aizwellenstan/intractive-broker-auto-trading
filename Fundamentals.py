from ib_insync import *
from bs4 import BeautifulSoup as bs

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

contract = Stock('AAPL', 'SMART', 'USD')

fundamentals =  ib.reqFundamentalData(contract, 'ReportSnapshot')

# print(fundamentals)

"""cmd 
python Fundamentals.py > fundamentals.txt
"""

content = bs(fundamentals, "xml")

print(content)

ratios = content.find_all("Ratio")

for ratio in ratios:
    print(ratio['FieldName'])
    print(ratio.text)