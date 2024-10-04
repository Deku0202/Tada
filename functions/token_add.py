import requests
from functions import mainfuns
from functions.headers import login_headers
import json
import os

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