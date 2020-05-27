def domain_name(url):
    if 'https' in url:
        if url.index('http')<4:
            url=url.replace('https://','')
    elif 'http' in url:
        if url.index('http')<4:
            url=url.replace('http://','')
    if 'www' in url:
        url=url.replace('www.','')
        url=url.split('.')
    else:
        url=url.split('.')
    return url[0]
