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
# from functions import task



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
            
            #choose option to do
            mainfuns.log(f"{mainfuns.green}Buy all Skins: {mainfuns.white}1")
            mainfuns.log(f"{mainfuns.green}Complete Tasks: {mainfuns.white}2")

            #choose
            print(f"{green}Choose: {reset}", end='')
            option = int(input())
            
            #if statement for choosing option
            if option == 1:
                total_skin = 39
    
                #loop the buying skin
                for i in range(total_skin):
                                
                    skin_buy.skin(data, proxies, i)
            
            #check total task
            if option == 2:
                total_task = task.task_list(data, proxies)
                
                #Attempting and 2 seconds
                mainfuns.log(f"{mainfuns.green}Attempting to complete Tasks.")
                time.sleep(2)
                
                #take out only the Youtube and social meida tasks
                for selected_task in total_task:
                    if selected_task['isCompleted'] == False and ("invite_friends" not in selected_task['id']):
                        
                        task_id = selected_task['id']
                        task.check_task(data, proxies, task_id)
                        mainfuns.delay(5)


#running main function
if __name__ == "__main__":
    try:
        hamster = Hamster()
        hamster.main()
    except KeyboardInterrupt:
        sys.exit()