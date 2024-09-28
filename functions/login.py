import requests
from functions import mainfuns
from functions.headers import login_headers

#get the token 
def token(query, proxy):
    url = 'https://backend.clutchwalletserver.xyz/tada-ton/v1/auth/login'

    payload = {"initData":query}
    
    try:
        response = requests.post(
            url=url,
            headers=login_headers(),
            json=payload,
            proxies=proxy,
            timeout=20
        )
        
        data = response.json()
        
        return data["accessToken"]
        
        #print the total coin
        mainfuns.log(f"{mainfuns.green}Successfully access Token")
        
    except:
        return None



#request the user data
def info(data, proxy):
    url = 'https://api.hamsterkombatgame.io/interlude/sync'
    
    try:
        response = requests.post(
            url=url,
            headers=headers(data=data),
            proxies=proxy,
            timeout=20,
        )
        data = response.json()
        total_coins = data["interludeUser"]["balanceDiamonds"]
        
        #print the total coin
        mainfuns.log(f"{mainfuns.green}Total Coins: {mainfuns.white}{total_coins:.2f}")
        
        
    except:
        return None