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
#    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:89.0) Gecko/20100101 Firefox/89.0"
    config = get_config()
    cookie = config['cookie']
    headers = {'User_Agent': user_agent, 'Referer':'https://gu.qq.com', 'Connection':'keep-alive'}
    #headers = {'User-Agent': user_agent, 'Referer':'sina.cn', 'Connection':'keep-alive'}

    futurefile = csv.reader(open('./future.csv', 'r'))
    futuredata = list(futurefile)
    futurelen = len(futuredata)

    today = datetime.now()
    time_start = datetime(today.year, today.month, today.day, 9, 30, 0, 0)
    m = 11
    datalist = [0]*m*futurelen

    while 1:
        time.sleep(5)
        num = 0
        for i in range(futurelen-1):
            if futuredata[i+1][1][0] == '6':
                url = 'https://qt.gtimg.cn/?q=sh' + futuredata[i+1][1]+'?r=1643095048199'
            else:
                url = 'https://qt.gtimg.cn/?q=sz' + futuredata[i+1][1]+'?r=1643095048199'
                #url = 'https://hq.sinajs.cn/?_=0.8805962879382798&list=sz' + futuredata[i+1][1]
            #print(url)
            page = requests.get(url, headers=headers)
            page.encoding = 'utf-8'
            #print(page.text)
            data = page.text
            lists = data.split('~')
            #print(lists)
            v_now = float(lists[3])
            v_pre = float(lists[4])
            v_open = float(lists[5])
            v_high = float(lists[33])
            v_low = float(lists[34])
            zf_open = (v_open - v_pre) / v_pre * 100
            # if (-10.0 < zf_open < -7.0) or \
            if (-4.0 < zf_open < -3.0) or\
             (-3.0 < zf_open < -2.0) or\
             (-2.0 < zf_open < -1.0) or\
             (-1.0 < zf_open < 0.0) or\
             (-0.0 < zf_open < 1.0) :
                zf_now = (v_now - v_pre) / v_pre * 100
                good_level = round((v_low - v_open) / v_pre * 100, 2)
                now_level = round((v_now - v_open) / v_pre * 100, 2)
                datalist[num*m+0] = futuredata[i+1][1]
                datalist[num*m+1] = v_pre
                datalist[num*m+2] = v_open
                datalist[num*m+3] = round(zf_open,2)
                datalist[num*m+4] = v_now
                datalist[num*m+5] = round(zf_now,2)
                datalist[num*m+6] = v_high
                datalist[num*m+7] = v_low
                datalist[num*m+8] = good_level
                datalist[num*m+9] = now_level
                if v_high > v_open:
                    datalist[num*m+10] = 1
                num += 1
        os.system('clear')
        s = '{0:^4}\t{1:^4}\t{2:^4}\t{3:^4}\t{4:^4}\t{5:^4}\t{6:^5}\t{7:^5}\t{8:^4}\t{9:^4}\t{10:^2}'
        print(s.format("", 'pre', 'open','zf', 'now', 'zf','high','low','level', 'level', 'act'))

        for i in range(num):
          print(s.format(datalist[i*m], datalist[i*m+1],datalist[i*m+2],datalist[i*m+3],datalist[i*m+4],datalist[i*m+5],datalist[i*m+6],datalist[i*m+7],\
          datalist[i*m+8],datalist[i*m+9],datalist[i*m+10]))

          # out = []
          # for j in range(10):
          #   out.append(datalist[i*m+j])
          # print(s.format(out))
            
 
    
