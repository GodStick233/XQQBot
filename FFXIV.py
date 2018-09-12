import requests
import re
import json
URL = 'https://ff14.huijiwiki.com/wiki/'
ITEMS = 'https://ff14.huijiwiki.com/wiki/物品:'
def searchwiki(wiki):
    end = URL + wiki
    return end

def searchitems(wiki):
    end = ITEMS + wiki
    return end

def searchget(wiki):
    kv = {'user-agent': 'Mozilla/5.0'}
    url = URL + wiki
    html = requests.get(url, headers=kv)
    patten = re.compile('<a.*?title="(.*?)">.*?</a></div>', re.S)
    items = re.findall(patten, html.text)
    items = items[5:]
    ask = '战力品有：'
    for i in items:
        ask = ask +','+ i
    return ask
