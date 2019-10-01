# import libraries
import csv
from fetch import fetchThisStock

###  --------    Read Stock code from file  --------
## Old code
# stocklist = []
# f = open("SGXCode10", "r")
# for x in f:
#     stocklist.append(x.rstrip())
# f.close()
# print(stocklist)

# input get from https://www2.sgx.com/securities/stock-screener
stocklist = []
with open('input_small.csv', 'r') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        stocklist.append(row)
csvFile.close()
print(stocklist)
###  --------    Read Stock code from file  --------


##  --------    Write To CSV  --------
with open('ParsedData.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(
        ["Name", "Code", "Industry", "Price", "Day Change", "Day Change %", "EPS", "BETA75", "BETA500", "EBITDA", "EV",
         "PSALES", "PBOOK", "ROE", "OM", "DIV"])

    for oneStock in stocklist:
        response = fetchThisStock(oneStock[1])
        if response:
            writer.writerow(oneStock + response)

csvFile.close()
