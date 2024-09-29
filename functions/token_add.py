import requests
from functions import mainfuns
from functions.headers import login_headers
import json
import os

def token_add(data):
    
    main_dir = os.path.dirname(os.path.realpath(__file__))
    
    # Get the directory of the data file
    data_dir = os.path.join(main_dir, "token.json")
    
    #load the accounts
    accounts = json.load(open(data_dir, "r"))
    total_acc = len(accounts)
    
    if total_acc == 0:
        key = str(total_acc)
        
    else:
        key = str(total_acc + 1)
    
    add_account(key, data)
    
    return
        

def add_account(account_name, account_value):
    
    main_dir = os.path.dirname(os.path.realpath(__file__))

    # Get the directory of the data file
    data_dir = os.path.join(main_dir, "token.json")

    
    #load the accounts
    existing_data = json.load(open(data_dir, "r"))
        
    # Add the new account data
    existing_data[account_name] = account_value
    
    # Write the updated data back to the file
    with open(data_dir, 'w') as json_file:
        json.dump(existing_data, json_file, indent=4)