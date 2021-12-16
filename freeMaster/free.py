#ecoding=utf-8
import tushare as ts
import csv
import time
import pdb
import pandas as pd

csv_file = csv.reader(open('./data/list.csv', 'r'))
filedata = list(csv_file)

buytime = 0
suctime2 = 0
suctime3 = 0
suctime = 0
getv = 0
for codeinfo in filedata:
    idx = filedata.index(codeinfo)
    name = './data/' + codeinfo[0]
    codedata = list(csv.reader(open(name, 'r')))

    datalen = len(codedata)
    changesh = 9.0
    num = 5 + 1
    for i in range(7, datalen-num-1):
        dailydata = codedata[datalen-1-i]
        if float(dailydata[3]) >20.0 or float(dailydata[3]) <10.0:
           continue
        d0 = float(dailydata[9])
        if d0 > changesh:
            d1 = float(codedata[datalen-1-i-1][9])
            d2 = float(codedata[datalen-1-i-2][9])
            d3 = float(codedata[datalen-1-i-3][9])
            
            v1 = float(codedata[datalen-1-i+1][9])
            v2 = float(codedata[datalen-1-i+2][9])
            v3 = float(codedata[datalen-1-i+3][9])
            v4 = float(codedata[datalen-1-i+4][9])
            v5 = float(codedata[datalen-1-i+5][9])
            v6 = float(codedata[datalen-1-i+6][9])

            vsum = d0 + d1 + v1 +v2 + v3 + v4 + v5 + v6

            vs = float(codedata[datalen-1-i-2][3])
            vs0 = float(codedata[datalen-1-i-2][7])
            ve = float(codedata[datalen-1-i-2][4])
            if  d1 > 9.0:
                if vs != ve and vs > vs0:# and vsum < 80.0:# and (vs -vs0)/vs0 < 0.05:
                    buytime+=1
                    getv = getv + d2 +d3 
                    if d3+d2 > 0.0:
                        suctime +=1
                        #print(dailydata)
                        #print(codedata[datalen-1-i-1])
                        #print(codedata[datalen-1-i-2])
#                        print((vs-vs0)/vs0)
                        #print(codedata[datalen-1-i-3])
                    if d2 > 0.0:
                        suctime2 +=1
                    if d3 > 0.0:
                        suctime3 +=1

print(buytime)
print(suctime)
print(suctime2)
print(suctime3)
print(float(suctime)/float(buytime))
print(getv)
print(getv/buytime)

list0 = []
for codeinfo in filedata:
    name = './data/' + codeinfo[0]
    codedata = list(csv.reader(open(name, 'r')))
    if float(codedata[2][3]) > 20.0 or float(codedata[2][3]) < 10.0:
        continue
    d1 = float(codedata[1][9])
    d2 = float(codedata[2][9])
    
    if  d1 > 9.0 and d2 > 9.0:
        list0.append(codeinfo[0][0:6])

outlist = [[] for i in range(len(list0))]
for i in range(len(list0)):
    outlist[i].append(list0[i])

out=pd.DataFrame(data=outlist)
out.to_csv('./future.csv', encoding='utf-8')
    
