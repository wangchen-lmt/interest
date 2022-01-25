#ecoding=utf-8
import tushare as ts
import csv
import time
import datetime
import pdb
import pandas as pd

csv_file = csv.reader(open('./data/list.csv', 'r'))
filedata = list(csv_file)

# start wealth
wealth = 2
# busy wealth
busy_wealth = 0
# free wealth
idle_wealth = 2
use_wealth = 0
# code in hand
hand_code = []
# each value of code in hand
hand_value = []

buytime = 0
suctime = 0
income_list = []

date_start = '20190101'
date_end = '20211227'


time_start = datetime.datetime.strptime(date_start, "%Y%m%d")
time_end = datetime.datetime.strptime(date_end, "%Y%m%d")
while(time_start < time_end):
  time_start = time_start + datetime.timedelta(days=1)
  timeuse = datetime.datetime.strftime(time_start, "%Y%m%d")
  print(timeuse)

  # find code valid
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
            l0 = float(dailydata[5])
            e0 = float(codedata[datalen-1-i-1][6])
         
            low = (l0 - s0)/e1*100

            if d1 >9.9 and d2 > 9.9 and s0!=h0 and 0 < abs(low) < 5.0:
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

  ##sell code in hand
  temp_hand_code = []
  temp_hand_value = []
  sell_wealth = 0
  if len(hand_code) > 0:
    for k in range(len(hand_code)):
      name = './data/' + hand_code[k]
      codedata = list(csv.reader(open(name, 'r')))
      datalen = len(codedata)
      sell_fail = 1
      for i in range(2, datalen-2):
          dailydata = codedata[datalen-1-i]
          if dailydata[2] == timeuse:
            e0 = float(dailydata[6])
            s0 = float(codedata[datalen-1-i+1][3])
            sell_wealth += hand_value[k]*(1+(e0-s0)/s0)
            sell_fail = 0

      if sell_fail:
        temp_hand_code.append(hand_code[k])
        temp_hand_value.append(hand_value[k])
  
  ## update hand code
  hand_code = temp_hand_code
  hand_value = temp_hand_value
  
  ## buy code
  code_num = len(codelist)
  print(code_num)
  if code_num > 0:
    # use half wealth to buy 
    if busy_wealth < wealth/2:
      use_wealth = wealth/2
    else:
      use_wealth = idle_wealth
    for j in range(code_num):
      name1 = './data/' + codelist[j]
      codedata1 = list(csv.reader(open(name1, 'r')))
      # save hand code and value
      hand_code.append(codelist[j])
      hand_value.append(use_wealth/code_num)
    # update idle wealth after buy
    idle_wealth -=use_wealth
  print(hand_code)

  #update busy wealth
  busy_wealth = 0
  for i in range(len(hand_code)):
    busy_wealth += hand_value[i]
  

    # print(codedata1[datalen1-1-idxlist[j]+1])
    # print(codedata1[datalen1-1-idxlist[j]+2])
    # print(codedata1[datalen1-1-idxlist[j]])
    # print(codedata1[datalen1-1-idxlist[j]-1])

  ## update wealth
  # update idle after sell
  idle_wealth += sell_wealth

  wealth = busy_wealth + idle_wealth
  print(wealth, busy_wealth, idle_wealth)         
  income_list.append(wealth)
print(buytime)
print(float(suctime)/float(buytime))
print(wealth)
print(wealth/buytime)

outlist = [[] for i in range(len(income_list))]
for i in range(len(income_list)):
    outlist[i].append(income_list[i])

out=pd.DataFrame(data=outlist)
out.to_csv('./income.csv', encoding='utf-8')

    
