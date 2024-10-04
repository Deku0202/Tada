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
import readline

from functions import mainfuns
from functions import login
from functions import task
from functions import token_add
from functions import query



red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
black = Fore.LIGHTBLACK_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL

class Tada:
    def __init__(self):
        # Get the directory where the script is located
        self.main_dir = os.path.dirname(os.path.realpath(__file__))

        # Get the directory of the data file
        self.data_dir = os.path.join(self.main_dir, "functions/token.json")
        
        self.proxy_dir = os.path.join(self.main_dir, "proxy.json")

        # Get the directory of the config file
        self.config = os.path.join(self.main_dir, "config.json")

    def main(self): 
        
        #load the accounts
        accounts = json.load(open(self.data_dir, "r"))
        proxy = json.load(open(self.proxy_dir, "r"))
        total_acc = len(accounts)
        proxy_len = len(proxy)
        
        random_num = random.randrange(0,proxy_len)
        proxy = proxy[str(random_num)]
        
        # proxy = proxy[0]['proxy_info']
        #proxy with http and https format
        proxies = mainfuns.format_proxy(proxy)
                
        #choose option to do
        mainfuns.log(f"{mainfuns.green}Add Data: {mainfuns.white}1")
        mainfuns.log(f"{mainfuns.green}Complete Tasks: {mainfuns.white}2")

        #choose
        print(f"{green}Choose: {reset}", end='')
        option = int(input())
        
        #if statement for choosing option
        if option == 1:
            
            #check if there data already
            mainfuns.token_chk()
                
            while True:
                #choose
                print(f"{green}Add Query ID: {reset}", end='')
                data = input()
                
                query_id = query.query_id(data)
                    
                #information
                token = login.token(query_id, proxies)
                    
                token_add.token_add(token)
        
        elif option == 2:
        
            #print the total account
            mainfuns.log(f"{green}Total Account: {white}{total_acc}")
            
            #proxy check if valid or not 
            for num, acc in enumerate(accounts):
                mainfuns.log(f"{green}Account Number: {white}{num+1}")
                data = accounts[acc]
                proxy_info = mainfuns.proxy(proxy)
                if proxy_info is None:
                    break
                
                #proxy ip
                proxy_ip = mainfuns.check_ip(proxy)
                
                #proxy with http and https format
                proxies = mainfuns.format_proxy(proxy)
                
                #check total tasks
                total_tasks = task.task_list(data, proxies)
                    
                if total_tasks == None:
                    break
                    
                #finish the tasks
                for i in total_tasks:
                        
                    if i['slug'] == "miniapp_telegram_channel_follow":
                        continue
                        
                    if i['maxAccomplishCountPerUser'] is None or i['userClaimableAccomplishmentsCount'] > 0 or i['maxAccomplishCountPerUser'] > i['userAccomplishedCount']:
                        if i['activityTypes'] is None and 'Invite' not in i['name']:
                            task.finish_task(data, proxies, i['id'], i['name'])
                        elif 'Invite' not in i['name']:
                            task.check_task(data, proxies,i['activityTypes'][0], i['id'], i['name'])


#running main function
if __name__ == "__main__":
    try:
        tada= Tada()
        tada.main()
    except KeyboardInterrupt:
        sys.exit()