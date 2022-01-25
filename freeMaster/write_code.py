#ecoding=utf-8
#import mysql.connector
import tushare as ts
import csv

pro = ts.pro_api('42619e72dfa3e36928266716519960a3e56249cea06b0bdf0ac71340')
data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry')

csv_f = open('code.csv', 'w', encoding='utf-8')
data.to_csv('code.csv')
