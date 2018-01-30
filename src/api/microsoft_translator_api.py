'''
Created on 2018年1月26日

@author: Ming_Wu
'''

import json
import http.client, urllib.parse
import xml.etree.ElementTree as ET

host = 'api.microsofttranslator.com'
path = '/V2/Http.svc/Translate'
    
def getConfig():
    data = json.load(open('client_secret.json'))
    return data["serverkey"]

def tanslateWithTarget(text, target):
    key = getConfig()
    headers = {'Ocp-Apim-Subscription-Key': key}
    
    params = '?to=' + target + '&text=' + urllib.parse.quote(text)
    conn = http.client.HTTPSConnection(host)
    conn.request("GET", path + params, None, headers)
    response = conn.getresponse()
    
    tree = ET.parse(response)
    root = tree.getroot()
    return root.text

"""
language symbols:
[u'ar', u'bg', u'ca', u'zh-CHS', u'zh-CHT', u'cs', u'da', u'nl', u'en', 
u'et', u'fi', u'fr', u'de', u'el', u'ht', u'he', u'hi', u'mww', u'hu', 
u'id', u'it', u'ja', u'tlh', u'tlh-Qaak', u'ko', u'lv', u'lt', u'ms', 
u'mt', u'no', u'fa', u'pl', u'pt', u'ro', u'ru', u'sk', u'sl', u'es', 
u'sv', u'th', u'tr', u'uk', u'ur', u'vi', u'cy']
""" 
def main():
    target = 'zh-CHT'
    text = 'Hello World'
    result = tanslateWithTarget(text, target)
    print(result)
#     defaultTranslate()

    
if __name__ == '__main__':
    main()
