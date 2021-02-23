from ib_insync import *
import io, sys

ib = IB()
ib.connect('127.0.0.1', 7497, clientId=1)

allParams = ib.reqScannerParameters()
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8') 
print(allParams)

"""
"STK",
"STOCK.HK",
"STOCK.EU"
"STK.US",
"STK.US.MAJOR",
"STK.US.MINOR",
"STK.HK.SEHK",
"STK.HK.ASX",
"STK.EU"
"FUT.GLOBEX"

scanCode

"LOW_OPT_VOL_PUT_CALL_RATIO",
"HIGH_OPT_IMP_VOLAT_OVER_HIST",
"LOW_OPT_IMP_VOLAT_OVER_HIST",
"HIGH_OPT_IMP_VOLAT",
"TOP_OPT_IMP_VOLAT_GAIN",
"TOP_OPT_IMP_VOLAT_LOSE",
"HIGH_OPT_VOLUME_PUT_CALL_RATIO",
"LOW_OPT_VOLUME_PUT_CALL_RATIO",
"OPT_VOLUME_MOST_ACTIVE",
"HOT_BY_OPT_VOLUME",
"HIGH_OPT_OPEN_INTEREST_PUT_CALL_RATIO",
"LOW_OPT_OPEN_INTEREST_PUT_CALL_RATIO",
"TOP_PERC_GAIN",
"MOST_ACTIVE",
"TOP_PERC_LOSE",
"HOT_BY_VOLUME",
"TOP_PERC_GAIN",
"HOT_BY_PRICE",
"TOP_TRADE_COUNT",
"TOP_TRADE_RATE",
"TOP_PRICE_RANGE",
"HOT_BY_PRICE_RANGE",
"TOP_VOLUME_RATE",
"LOW_OPT_IMP_VOLAT",
"OPT_OPEN_INTEREST_MOST_ACTIVE",
"NOT_OPEN",
"HALTED",
"TOP_OPEN_PERC_GAIN",
"TOP_OPEN_PERC_LOSE",
"HIGH_OPEN_GAP",
"LOW_OPEN_GAP",
"LOW_OPT_IMP_VOLAT",
"TOP_OPT_IMP_VOLAT_GAIN",
"TOP_OPT_IMP_VOLAT_LOSE",
"HIGH_VS_13W_HL",
"LOW_VS_13W_HL",
"HIGH_VS_26W_HL",
"LOW_VS_26W_HL",
"HIGH_VS_52W_HL",
"LOW_VS_52W_HL",
"HIGH_SYNTH_BID_REV_NAT_YIELD",
"LOW_SYNTH_BID_REV_NAT_YIELD"
"""
"""
subscription = ScannerSubscription(instrument='STK', 
                                    locationCode='STK.US.MAJOR', 
                                    scanCode='SCAN_currYrETFFYDividendYield_DESC')

scanData = ib.reqScannerData(subscription)

for scan in scanData:
    # print(scan)
    print(scan.contractDetails.contract.symbol)
"""