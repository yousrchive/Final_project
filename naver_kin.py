# 네이버 검색 API 예제 - 지식인 검색
import os
import sys
import urllib.request
import pyautogui
import pandas as pd
import re
import json

client_id = "V_nYKHysuvrECXKayiOY"
client_secret = "widIdEMNm7"

encText = urllib.parse.quote(pyautogui.prompt("검색어를 입력하세요."))
idx = 0
display = 100
start = 1
end = 1000
sort = "sim"

kin_df = pd.DataFrame(columns=("Title", "Link", "Description"))

for start_index in range(start, end, display):
    
    url = "https://openapi.naver.com/v1/search/kin?query=" + encText \
        + "&display=" + str(display) \
        + "&start=" + str(start_index) \
        + "&sort=" + sort
    
request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
response = urllib.request.urlopen(request)
rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    response_dict = json.loads(response_body.decode('utf-8'))
    items = response_dict['items']
    for item_index in range(0, len(items)):
        remove_tag = re.compile('<.*?>')
        title = re.sub(remove_tag, '', items[item_index]['title'])
        link = items[item_index]['link']
        description = re.sub(remove_tag, '', items[item_index]['description'])
        kin_df.loc[idx] = [title, link, description]
        idx += 1
    else:
        print("Error Code:" + str(rescode))
        
kin_df

#여기 딱 키워드가 정확히 들어있을 때만 가져오면 좋을 듯