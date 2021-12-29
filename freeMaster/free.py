#ecoding=utf-8
import tushare as ts
import csv
import time
import pdb
import pandas as pd

csv_file = csv.reader(open('./data/list.csv', 'r'))
filedata = list(csv_file)

# for mmin in range(-10, 9, 1):
#     mmax = mmin + 1
buytime = 0
suctime = 0
d2_end = [0]*3
end_income = [0]*3
start_income = [0]*3
all_income = 0
for codeinfo in filedata:
    idx = filedata.index(codeinfo)
    name = './data/' + codeinfo[0]
    codedata = list(csv.reader(open(name, 'r')))

    datalen = len(codedata)
    num = 5 + 1
    for i in range(7, datalen-num-1):
        dailydata = codedata[datalen-1-i]
        #if float(dailydata[3]) >10.0 :# or float(dailydata[3]) <10.0:
          # continue
        d0 = float(dailydata[9])
        d1 = float(codedata[datalen-1-i-1][9])
        d2 = float(codedata[datalen-1-i-2][9])
        d3 = float(codedata[datalen-1-i-3][9])
        
        s0 = float(codedata[datalen-1-i-0][3])
        s1 = float(codedata[datalen-1-i-1][3])
        s2 = float(codedata[datalen-1-i-2][3])
        s3 = float(codedata[datalen-1-i-3][3])

        h2 = float(codedata[datalen-1-i-2][4])
        
        e0 = float(codedata[datalen-1-i-0][6])
        e1 = float(codedata[datalen-1-i-1][6])
        e2 = float(codedata[datalen-1-i-2][6])
        e3 = float(codedata[datalen-1-i-3][6])

        if d0 >9.9 and d1 > 9.9 and s2!=h2:
          
          if (-10.0 < (s2 - e1)/e1*100 < -7.0) or \
             (-4.0 < (s2 - e1)/e1*100 < -3.0) or\
             (-3.0 < (s2 - e1)/e1*100 < -2.0) or\
             (-2.0 < (s2 - e1)/e1*100 < -1.0) or\
             (-1.0 < (s2 - e1)/e1*100 < 0.0) or\
             (-0.0 < (s2 - e1)/e1*100 < 1.0) :
    
            buytime+=1
            all_income += (e3 - s2)/s2*100

            if e3>s2:
                suctime+=1

            if d2 > 9.9:
                d2_end[2] += 1
                end_income[2] += (e3 - s2)/s2*100
                start_income[2] += (s3 - s2)/s2*100

            elif d2 >=0.0:
                d2_end[1] += 1
                end_income[1] += (e3 - s2)/s2*100
                start_income[1] += (s3 - s2)/s2*100
                
            else:
                d2_end[0] += 1
                end_income[0] += (e3 - s2)/s2*100
                start_income[0] += (s3 - s2)/s2*100
              
# print(mmin, mmax)
print(buytime)
print(suctime)
if buytime != 0:
  print(float(suctime)/float(buytime))
  print(all_income)
  print(all_income/buytime)

print(d2_end)
print(end_income)
print(start_income)

list0 = []
for codeinfo in filedata:
    name = './data/' + codeinfo[0]
    codedata = list(csv.reader(open(name, 'r')))
    d1 = float(codedata[1][9])
    d2 = float(codedata[2][9])
    
    if  d1 > 9.9 and d2 > 9.9:
        list0.append(codeinfo[0][0:6])

outlist = [[] for i in range(len(list0))]
for i in range(len(list0)):
    outlist[i].append(list0[i])

out=pd.DataFrame(data=outlist)
out.to_csv('./future.csv', encoding='utf-8')
    
