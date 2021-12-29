#coding=utf-8
import requests
import json
import time
import matplotlib.pyplot as plt
from datetime import datetime
import os

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
    objs = config['obj']

    plt.ion()
    #plt.figure(1).patch.set_facecolor('black')
    plt.rcParams['axes.facecolor'] = 'w'
    t=[[] for i in range(len(objs))]
    v=[[] for i in range(len(objs))]
    #print(len(objs))
    i = 0
    time_idx = 0
    today = datetime.now()
    time_start = datetime(today.year, today.month, today.day, 9, 30, 0, 0)
    m = 4
    datalist = [0]*m*len(objs)
    lnlist = [0]*len(objs)
    while 1:
        time.sleep(5)
        #plt.clf()
        i = 0
        for url in objs:
            page = requests.get(url, headers=headers)
            page.encoding = 'utf-8'
            data = page.text.strip("var hq_str_sz000000=")
            lists = data.split(',')
#            print(lists)
            v_now = float(lists[3])
            v_start = float(lists[2])
            bfb = (v_now - v_start) / v_start * 100
            datalist[i*m] = lists[2]
            datalist[i*m+1] = lists[3]
            datalist[i*m+2] = round(bfb,2)
            datalist[i*m+3] = (int(lists[8]) - lnlist[i])/1000000
            lnlist[i] = int(lists[8])
            i = i+1
           # print(lists[2], lists[3], round(bfb,2))
        i = 0
        os.system('clear')
        for url in objs:
            print(datalist[i*m], datalist[i*m+1], datalist[i*m+2])
            i=i+1
           # time_now = datetime.now()
           # time_idx = (time_now - time_start).seconds
           # t[i].append(time_idx)
           # v[i].append(v_now)
            
           # plt.plot(t[i][:],v[i][:],'-b')
          #  i = i + 1
            
         #   name = page.text[11:17]
        #    plt.xlim((0, 19800))
       #     plt.ylim((v_start*0.9, v_start*1.1))
      #      plt.legend([lists[3] + "|" + str(round(bfb,2))], loc='upper right')
     #       plt.savefig(name+'.png', format='png')
            
 
    
