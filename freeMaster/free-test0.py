#ecoding=utf-8
import tushare as ts
import csv
import time
import datetime
import pdb
import pandas as pd

csv_file = csv.reader(open('./data/list.csv', 'r'))
filedata = list(csv_file)

buytime = 0
suctime = 0
all_income = 1
income_list = []

date_start = '20190101'
date_end = '20211227'


time_start = datetime.datetime.strptime(date_start, "%Y%m%d")
time_end = datetime.datetime.strptime(date_end, "%Y%m%d")
while(time_start < time_end):
  time_start = time_start + datetime.timedelta(days=2)
  timeuse = datetime.datetime.strftime(time_start, "%Y%m%d")
  print(timeuse)
  codelist = []
  idxlist = []
  for codeinfo in filedata:
      name = './data/' + codeinfo[0]
      codedata = list(csv.reader(open(name, 'r')))

      datalen = len(codedata)
      for i in range(2, datalen-2):

          dailydata = codedata[datalen-1-i]
          if dailydata[2] == timeuse:
            d1 = float(codedata[datalen-1-i+1][9])
            e1 = float(codedata[datalen-1-i+1][6])
            d2 = float(codedata[datalen-1-i+2][9])
            s0 = float(dailydata[3])
            h0 = float(dailydata[4])
            e0 = float(codedata[datalen-1-i-1][6])
         

            if d1 >9.9 and d2 > 9.9 and s0!=h0:
              if (-10.0 < (s0 - e1)/e1*100 < -7.0) or \
                (-4.0 < (s0 - e1)/e1*100 < -3.0) or\
                (-3.0 < (s0 - e1)/e1*100 < -2.0) or\
                (-2.0 < (s0 - e1)/e1*100 < -1.0) or\
                (-1.0 < (s0 - e1)/e1*100 < 0.0) or\
                (-0.0 < (s0 - e1)/e1*100 < 1.0) :
                codelist.append(codeinfo[0])
                idxlist.append(i)
                buytime+=1
                if e0>s0:
                    suctime+=1

  code_num = len(codelist)
  print(code_num)
  if code_num == 0:
    continue

  temp_income = all_income
  all_income = 0
  for j in range(code_num):
    name1 = './data/' + codelist[j]
    codedata1 = list(csv.reader(open(name1, 'r')))
    datalen1 = len(codedata1)
    
    s0 = float(codedata1[datalen1-1-idxlist[j]][3])
    e0 = float(codedata1[datalen1-1-idxlist[j]-1][6])
    # print(codedata1[datalen1-1-idxlist[j]+1])
    # print(codedata1[datalen1-1-idxlist[j]+2])
    # print(codedata1[datalen1-1-idxlist[j]])
    # print(codedata1[datalen1-1-idxlist[j]-1])

    print(s0, e0)
    all_income += temp_income/code_num*(1+(e0-s0)/s0)
  print(all_income)         
  income_list.append(all_income)

print(buytime)
print(float(suctime)/float(buytime))
print(all_income)
print(all_income/buytime)

outlist = [[] for i in range(len(income_list))]
for i in range(len(income_list)):
    outlist[i].append(income_list[i])

out=pd.DataFrame(data=outlist)
out.to_csv('./income0.csv', encoding='utf-8')

    
