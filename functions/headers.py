def login_headers():
    headers = {
        "accept": "application/json, text/plain, */*",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
        "content-type": "application/json",
        "origin": "https://tada-mini.mvlchain.io",
        "x-requested-with": "org.telegram.messenger",
        "sec-fetch-site": "same-site",
        "sec-fetch-mode": "cors",
        "sec-fetch-dest": "empty",
        "referer": "https://tada-mini.mvlchain.io/",
        "accept-encoding": "gzip, deflate",
        "accept-language": "en,en-US;q=0.9",
    }
    return headers

def task_headers(data):
    headers = {
        "Accept": "application/json, text/plain, */*",
        "Origin": "https://tada-mini.mvlchain.io",
        "Referer": "https://tada-mini.mvlchain.io/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
        "Authorization": f"Bearer {data}",
    }
    return headers

