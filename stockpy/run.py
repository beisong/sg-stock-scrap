# import libraries
import csv
from fetch import fetchThisStock

import logging

logging.basicConfig(filename='debug.log', level=logging.INFO)

###  --------    Read Stock code from file  --------
# input get from https://www2.sgx.com/securities/stock-screener
stocklist = []
with open('input.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        stocklist.append(row)
csvFile.close()
# print(stocklist)
###  --------    Read Stock code from file  --------


##  --------    Write To CSV  --------
with open('ParsedData.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(
        ["Name", "Code", "Industry", "Price", "Day Change", "Day Change %", "EPS", "BETA75", "BETA500", "EBITDA",
         "Enterprise Value", "Price to Sales", "Price to Book", "Return on Equity", "Operating Margins",
         "Dividend ($)"])

    for oneStock in stocklist:
        print(oneStock[1])
        logging.info(oneStock[1])
        response = fetchThisStock(oneStock[1])
        if response:
            writer.writerow(oneStock + response)

csvFile.close()
