import requests
import time
from functions import mainfuns
from functions.headers import task_headers


#Dict for the task name
task_names = {
    'youtube': 'Youtube Ads',
    'facebook': 'Follow on Facebook',
    'telegram': 'Subscribe telegram Channel',
    'x': 'Follow on Twitter',
    'instagram': 'Follow on Instagram'
}

#check test name 
def task_name(id):
    for task_name in task_names:
        if task_name in id:
            return task_names[task_name]


#request the tasks
def task_list(data, proxy):
    url = 'https://backend.clutchwalletserver.xyz/activity/v2/missions?missionGroupId=eea00000-0000-4000-0000-000000000000&excludeAutoClaimable=true'
    
    payload = 'missionGroupId=eea00000-0000-4000-0000-000000000000&excludeAutoClaimable=true'
    
    try:
        response = requests.get(
            url=url,
            headers=task_headers(data=data),
            data=payload,
            proxies=proxy,
            timeout=20,
        )
        data = response.json()
        
        try:
            if data['message'] == 'Expired jwt token!':
                #expired token
                mainfuns.log(f"{mainfuns.red}Token Expired!")
                return None
            
        except:
            return data

        
    except:
        mainfuns.log(f"{mainfuns.red}Error connect to owner")
        return None
    
def finish_task(data, proxy, taskid, name):
    url =f'https://backend.clutchwalletserver.xyz/activity/v2/missions/{taskid}/claim'
    
    try:
        response = requests.post(
            url=url,
            headers=task_headers(data=data),
            proxies=proxy,
            timeout=20
        )
        
        result = response.json()
        
        length = len(result['missionPointTransactions'])
        
        if len(result['missionPointTransactions']) == 1:
            mainfuns.log(f"{mainfuns.white}{name}: {mainfuns.green}Completed")
            mainfuns.delay(5)
        
        return 

    except:
        mainfuns.log(f"{mainfuns.red}Error connect to owner")
        return None
    
#check the task
def check_task(data, proxy, taskname, taskid, name):
    url =f'https://backend.clutchwalletserver.xyz/activity/v3/activities/{taskname}'
    
    try:
        response = requests.post(
            url=url,
            headers=task_headers(data=data),
            proxies=proxy,
            timeout=20
        )
        
        result = response.json()
        
        if result['status'] =='ok':
            finish_task(data,proxy,taskid, name)
            
        return 
    
        
    except:
        mainfuns.log(f"{mainfuns.red}Error connect to owner")
        return None