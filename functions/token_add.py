import requests
from functions import mainfuns
from functions.headers import login_headers
from functions.headers import task_headers
import json
import os
from time import time
import jwt

#put the token to the token.json
def token_add(account_name, account_refresh):
    
    main_dir = os.path.dirname(os.path.realpath(__file__))

    # Get the directory of the data file
    data_dir = os.path.join(main_dir, "token.json")

    account_value = {
        'token': account_name,
        'refresh': account_refresh
        }
    
    #load the accounts
    existing_data = json.load(open(data_dir, "r"))
        
    # Add the new account data
    existing_data["accounts"].append(account_value)
    
    # Write the updated data back to the file
    with open(data_dir, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)
        
    return

#check token expired  or not
def is_token_expired(token):
    decode = jwt.decode(token, options={"verify_signature": False})
    exp_time = decode.get('exp')
    current = time()
    
    return current > exp_time

#refresh the tokens
def token_refresh(refresh, proxy, num, count):
    
    url =f'https://backend.clutchwalletserver.xyz/v2/accounts/sessions/refresh'
    
    try:
        response = requests.post(
            url=url,
            headers=task_headers(data=refresh),
            proxies=proxy,
            timeout=20
        )
        
        result = response.json()
        
        #replace the new data into the token.json
        main_dir = os.path.dirname(os.path.realpath(__file__))

        # Get the directory of the data file
        data_dir = os.path.join(main_dir, "token.json")
        
        #load the accounts
        existing_data = json.load(open(data_dir, "r"))
        
        #change the value 
        existing_data["accounts"][num]['token'] = result['accessToken']
        existing_data["accounts"][num]['refresh'] = result['refreshToken']
        
        # Write the updated data back to the file
        with open(data_dir, 'w') as json_file:
            json.dump(existing_data, json_file, indent=4)
        
        return result['accessToken']

    except:
        if count == 0:
            mainfuns.delay(3)
            return None
        mainfuns.log(f"{mainfuns.red}Error connect to owner")
        return None
    
    return