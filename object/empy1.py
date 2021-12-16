#coding=utf-8
import requests
import json
import time
from datetime import datetime
import os
import csv

def get_config():
    config_path = "config.json"
    with open(config_path) as f:
        config = json.loads(f.read())
        return config

if __name__ == '__main__':
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'

    config = get_config()
    cookie = config['cookie']
    headers = {'User_Agent': user_agent, 'Cookie': cookie}

    futurefile = csv.reader(open('./future.csv', 'r'))
    futuredata = list(futurefile)
    futurelen = len(futuredata)

    time_idx = 0
    today = datetime.now()
    time_start = datetime(today.year, today.month, today.day, 9, 30, 0, 0)
    m = 3
    datalist = [0]*m*futurelen

    while 1:
        time.sleep(5)
        num = 0
        for i in range(futurelen-1):
            if futuredata[i+1][1][0] == '6':
                url = 'https://hq.sinajs.cn/?_=0.8805962879382798&list=sh' + futuredata[i+1][1]
            else:
                url = 'https://hq.sinajs.cn/?_=0.8805962879382798&list=sz' + futuredata[i+1][1]
            #print(url)
            page = requests.get(url, headers=headers)
            page.encoding = 'utf-8'
            data = page.text.strip("var hq_str_sz000000=")
            lists = data.split(',')
            v_now = float(lists[3])
            v_start = float(lists[2])
            bfb = (v_now - v_start) / v_start * 100
        #    if bfb > 0.0:
         #       continue
            datalist[num*m] = futuredata[i+1][1]
            datalist[num*m+1] = v_now
            datalist[num*m+2] = bfb
            num += 1
           # print(lists[2], lists[3], round(bfb,2))
        os.system('clear')
        for i in range(num):
            print(datalist[i*m], datalist[i*m+1], datalist[i*m+2])
            
 
    
