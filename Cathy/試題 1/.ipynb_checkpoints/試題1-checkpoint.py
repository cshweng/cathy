# -*- coding: utf-8 -*-
"""
題目一
"""
# Import Library
from bs4 import BeautifulSoup
import requests
from urllib.request import urlopen as uReq
import json
import pandas as pd
import re
import ddddocr

# Define Parameter
url_1 = "https://www.ris.gov.tw/info-doorplate/app/doorplate/query"
url_2 = "https://www.ris.gov.tw/info-doorplate/app/doorplate/inquiry/date"

headers = {
          "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"
          }
cookies = {"cookies":"JSESSIONID=AAF584AD4D880B5AD93FCE47280F01FE.sris-aw-info-doorplate-3; \
           _ga=GA1.3.2002745824.1682738242; \
           JSESSIONID=770A404C5B8691FBE9D205436D9923C5.sris-aw-root-2; \
           _gid=GA1.3.1716816783.1682920561"
           
          }
payloadData_map = {
            "cityCode": "68000000",
            "searchType": "date",
            }

# Start Crawler
session = requests.Session()
result = session.post(url=url_1, headers=headers,cookies=cookies ,data=payloadData_map)
soup = BeautifulSoup(result.text, 'html.parser')

# GET CAPTCHA_KEY
a_tags = soup.find_all(value=re.compile("^[a-zA-Z0-9]{32}$"))
for tag in a_tags:
    CAP = (tag.get('value'))
print(CAP)

# download the CAPTCHA image
CAP_image = f"https://www.ris.gov.tw/info-doorplate/captcha/image?CAPTCHA_KEY={CAP}&time=1682931576385.jpeg"
print(CAP_image)

img_data = requests.get(CAP_image).content
with open('CAP_image.jpeg', 'wb') as handler:
    handler.write(img_data)

# CAPTCHA image Recognition
ocr = ddddocr.DdddOcr()
with open('CAP_image.jpeg', 'rb') as f:
    image_bytes = f.read()
res = ocr.classification(image_bytes)
print(res)

# define payload for query
payloadData = {
    "searchType": "date",
    "cityCode": 68000000,
    "tkt": -1,
    "areaCode": 68000010,
    "village": "",
    "neighbor": "",
    "sDate": "111-01-01",
    "eDate": str(datetime.date.today(),
    "_includeNoDate": "on",
    "registerKind": 0,
    "captchaInput": res,
    "captchaKey": CAP,
    "floor": "",
    "lane": "",
    "alley": "",
    "number": "",
    "number1": "",
    "ext": "",
    "_search": "false",
    "nd": 1682931576385,
    "rows": 50000,
    "page": 1,
    "sidx": "",
    "sord": "asc"
     }
result = session.post(url=url_2, headers=headers,cookies=cookies ,data=payloadData)
soup = BeautifulSoup(result.text, 'html.parser')

# Data Clearing
Map = pd.DataFrame({ "key" : ['1','2','3','4','5','6','7'],
                    "values" : ["門牌初編","門牌改編","門牌增編","門牌合併","門牌廢止","行政區域調整","門牌整編"]})
df = pd.DataFrame(json.loads(result.text)["rows"])
df = df.merge(Map,how='left', left_on="v3", right_on="key")
df = df.rename(columns={"v1":"門牌資料","v2":"編釘日期","values":"編釘類別"})[["門牌資料","編釘日期","編釘類別"]]
df

# Save data to csv
df.to_csv("試題1_CRAWLER.csv")

