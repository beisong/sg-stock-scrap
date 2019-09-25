from fetch import fetchThisStock

###  --------    Read Stock code from file  --------
stocklist = []
f = open("SGXCode50", "r")
for x in f:
    stocklist.append(x.rstrip())
f.close()
print(stocklist)
###  --------    Read Stock code from file  --------

for i in stocklist:
    print(i)
    fetchThisStock(i)





