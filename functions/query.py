import urllib.parse

#function to get the query id from raw link
def query_id(data):
    url = data
    
    raw_query = urllib.parse.unquote(url)
    
    first_half = raw_query.partition('&tgWebAppVersion')

    final = first_half[0].partition('tgWebAppData=')
    
    #if the data is already sliced
    if final[-1] == '':
        return data
    
    return final[-1]
