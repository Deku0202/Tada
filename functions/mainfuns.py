import os
import sys
from colorama import *
import json
from datetime import datetime
import requests
from requests.auth import HTTPProxyAuth
import time

red = Fore.LIGHTRED_EX
yellow = Fore.LIGHTYELLOW_EX
green = Fore.LIGHTGREEN_EX
black = Fore.LIGHTBLACK_EX
blue = Fore.LIGHTBLUE_EX
white = Fore.LIGHTWHITE_EX
reset = Style.RESET_ALL

#printing function
def log(msg):
    print(f"{msg}{reset}")
    
# Handle proxy version
def format_proxy(proxy_info):
    return {"http": f"{proxy_info}", "https": f"{proxy_info}"}
    
#proxy ip
def check_ip(proxy_info):
    url = "https://api.ipify.org?format=json"

    proxies = format_proxy(proxy_info=proxy_info)

        # Parse the proxy credentials if present
    if "@" in proxy_info:
        proxy = proxy_info.split('://',1)[-1]
        proxy_credentials = proxy.split("@")[0]
        proxy_user, proxy_pass = proxy_credentials.split(":")

        auth = HTTPProxyAuth(proxy_user, proxy_pass)
    else:
        auth = None

    try:
        response = requests.get(url=url, proxies=proxies, auth=auth)
        response.raise_for_status()  # Raises an error for bad status codes
        actual_ip = response.json().get("ip")
        log(f"{green}Actual IP Address: {white}{actual_ip}")
        return actual_ip
    
    except requests.exceptions.RequestException as e:
        log(f"{red}IP check failed: {white}{e}")
        return None

    
#proxy check
def proxy(proxy):
    try:
        domain = proxy.split('://',1)[-1]
        info, iport = domain.split('@', 1)
        username, password = info.split(":", 1)
        ip, port = iport.split(":", 1)
        return {"user_name": username, "pass": password, "ip": ip, "port": port}
    except:
        log(f"{red}Check proxy format: {white}http://user:pass@ip:port")
        return None
    
#timedelay add
def delay(seconds):
    
    while seconds >= 0:
        mins, secs = divmod(seconds, 60)
        timer = '{:02d}:{:02d}'.format(mins,secs)
        print(f"{timer}{reset}", end="\r") 
        time.sleep(1)
        seconds -= 1

    return