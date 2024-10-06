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
        
        return data["accessToken"], data["refreshToken"]
        
        #print the total coin
        mainfuns.log(f"{mainfuns.green}Successfully access Token")
        
    except:
        return None
