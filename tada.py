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
            # token = login.token(data, proxies)
            
            token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJkYzViZmQyZS1jYjEyLTRhMjMtYjUyYy1jMDBkMzk5YWJhOGMiLCJ0eXBlIjoiVEVMRUdSQU1fTUlOSUFQUCIsInVzZXJJZCI6IjU0MjEwNGM5LTEyN2UtNDUyYy04Y2NkLTExN2Y2M2YxYzIyMiIsInNpZCI6ImNiMzhmMjIxLTA5ZGItNGQ4My04NjI1LTdmYTVlMjAwN2FkZSIsIm5vbmNlIjoiak85S0ozU0YwYyIsImlhdCI6MTcyNzQ5MjkyMywiZXhwIjoxNzI3NTM2MTIzfQ.INWlnjtxP0OdvcWte9POVOgSFQozfO1w5PNiNlNr7hkn-Z0imB78N1G6a1ZqFn_ixFgnMtHje3Z56jfICXiv723BD3bH6XiFXuByok1_gaiatB-XVhpWygrEeKfN85OfoT9Iv-bhjkoUSTWK_91rf5px9g59wAp7j8jCBD-9IRVG97ETu6UXJaa25UyKtIiriZBW4BK9DIBTz07d9kWdsSpx8ttd9mTIzYIcJlWznDiCEjS_znPq3qSKQiBg8hoArqzZZIj6v85gXTDGT9LmxjpXPfxImvZuyuSSsAk0hQXm4ufplyam-UCbUSYIHv4vkYiikE7fu7picde5PtbPaCe3YoA543v1CYGnSGq5cdIaEYbpAhfT8OfBCzLahEh_qGJU4QCCzmZXUVUzyiTN_bhpxVRwUk7SBXWE2Qg2M0wjT8-02t8iChV5hHWL3g4GAemRagVtGAnplen2lO1yACpL7rnMkHXrfkSeaQLrON1hfa1NE39Te2no6Ir_q8wk1ESY27W2Q0Hjymn2NGO02UctN-ESdRUMq3BgMpGt2oqiVanEpCpQNRHiuvtW63FaKDODMtpBTJ2YUi1l06ahlxhoO4itDY8FUD6Vg_eNKvgJwfwIbQ49H2EaKHNmI3tIZUhE1VzMYf6IzAcHJ6ffAR9PZzmuGwiQlBcwRykvRL8'
            
            #check total tasks
            total_tasks = task.task_list(token, proxies)
            
            if total_tasks == None:
                break
            
            # task.check_task(token, proxies, "4d3a2841-d8fb-4cc8-98c2-9ebf1a70fe3b")
            # task.check_task(token, proxies,"open_gate_buy_mvl", "b32239cd-05d0-4d9e-accd-32865fdb4095","Buy $MVL in Gate.io")
            
            #finish the tasks
            for i in total_tasks:
                
                if i['slug'] == "miniapp_telegram_channel_follow":
                    break
                
                if i['maxAccomplishCountPerUser'] is None or i['userAccomplishedCount'] < i['maxAccomplishCountPerUser']:
                    if i['activityTypes'] is None and 'Invite' not in i['name']:
                        task.finish_task(token, proxies, i['id'], i['name'])
                    elif 'Invite' not in i['name']:
                        task.check_task(token, proxies,i['activityTypes'][0], i['id'], i['name'])
            
            
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