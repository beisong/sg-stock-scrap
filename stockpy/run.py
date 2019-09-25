# import libraries
import csv
from fetch import fetchThisStock

###  --------    Read Stock code from file  --------
stocklist = []
f = open("SGXCode", "r")
for x in f:
    stocklist.append(x.rstrip())
f.close()
print(stocklist)
###  --------    Read Stock code from file  --------


##  --------    Write To CSV  --------
with open('ParsedData.csv', 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(
        ["Name", "Code", "Price", "Day Change", "Day Change %", "EPS", "BETA75", "BETA500", "EBITDA", "EV", "PSALES",
         "PBOOK", "ROE", "OM", "DIV"])

    for i in stocklist:
        if fetchThisStock(i):
            print(i)
            writer.writerow(fetchThisStock(i))

csvFile.close()

# TODO GET VALUE FROM FETCH AND STORE IN CSV

# stockData = [STOCKNAME, code, PRICE, PERCENT_CHANGE, PRICE_CHANGE, EPS, BETA75, BETA500, EBITDA, EV, PSALES, PBOOK,ROE, OM, DIV]


# csvData = [['Person', 'Age'], ['Peter', '22'], ['Jasmine', '21'], ['Sam', '24']]
# with open('ParsedData.csv', 'w', newline='') as csvFile:
#     writer = csv.writer(csvFile)
#     writer.writerows(csvData)
# csvFile.close()
