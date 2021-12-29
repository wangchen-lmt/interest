#ecoding=utf-8
import tushare as ts
import csv
import time

pro = ts.pro_api('42619e72dfa3e36928266716519960a3e56249cea06b0bdf0ac71340')

csv_file = csv.reader(open('code.csv', 'r'))
filedata = list(csv_file)
for codeinfo in filedata:
    idx = filedata.index(codeinfo)
    if idx == 0 or codeinfo[1][0] == '8' or codeinfo[1][0:2] == '68':
        #print(codeinfo)
        continue
    print(idx)
    if idx % 500 == 0:
        time.sleep(61)        
    name = './data/' + codeinfo[2] + '.csv'
    csv_w = open(name, 'w', encoding='utf-8')
    today = time.strftime('%Y%m%d', time.localtime())
    codedata = pro.daily(ts_code=codeinfo[1], start_date='20190101', end_date=today)
    codedata.to_csv(name)

