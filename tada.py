import sys

#this will not produce bytecode from python
sys.dont_write_bytecode = True

import os 
import requests
from colorama import *
from requests.auth import HTTPProxyAuth
from datetime import datetime
import random
import json
import time

from functions import mainfuns
from functions import login
from functions import task



red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
black = Fore.LIGHTBLACK_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL

class Hamster:
    def __init__(self):
        # Get the directory where the script is located
        self.main_dir = os.path.dirname(os.path.realpath(__file__))

        # Get the directory of the data file
        self.data_dir = os.path.join(self.main_dir, "data.json")

        # Get the directory of the config file
        self.config = os.path.join(self.main_dir, "config.json")

    def main(self): 
        
        #load the accounts
        accounts = json.load(open(self.data_dir, "r"))['accounts']
        total_acc = len(accounts)
        
        
        #print the total account
        mainfuns.log(f"{green}Total Account: {white}{total_acc}")
        
        #proxy check if valid or not 
        for num, acc in enumerate(accounts):
            mainfuns.log(f"{green}Account Number: {white}{num+1}")
            data = acc['acc_info']
            proxy = acc['proxy_info']
            proxy_info = mainfuns.proxy(proxy)
            if proxy_info is None:
                break
            
            #proxy ip
            proxy_ip = mainfuns.check_ip(proxy)
            
            #proxy with http and https format
            proxies = mainfuns.format_proxy(proxy)
            
            #information
            token = login.token(data, proxies)
            
            #check total tasks
            total_tasks = task.task_list(token, proxies)
            
            if total_tasks == None:
                break
            
            #finish the tasks
            for i in total_tasks:
                
                if i['slug'] == "miniapp_telegram_channel_follow":
                    break
                
                if i['maxAccomplishCountPerUser'] is None or i['userAccomplishedCount'] < i['maxAccomplishCountPerUser']:
                    if i['activityTypes'] is None and 'Invite' not in i['name']:
                        task.finish_task(token, proxies, i['id'], i['name'])
                    elif 'Invite' not in i['name']:
                        task.check_task(token, proxies,i['activityTypes'][0], i['id'], i['name'])


#running main function
if __name__ == "__main__":
    try:
        hamster = Hamster()
        hamster.main()
    except KeyboardInterrupt:
        sys.exit()