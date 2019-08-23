import requests
import codecs
import csv
import io
#import prettytable
import json

key=input("關鍵字:")
page="1"
while key != "0":
    if page=="0":
        break
    else:
        p=requests.get(
            "https://ecshweb.pchome.com.tw/search/v3.3/all/results?",
            params={
            "q":key,
            "page":page,
            "sort":"sale/dc"
            }
        )
        p.encoding="utf8"
        j=json.loads(p.text)
        r=p.status_code
        if r!=200:
            print(r)

        #print(j["prods"][0]["name"],j["prods"][1]["name"])
        for i in j["prods"]:
            name=i["name"]
            price=i["price"]
            print(name,price)

        page=input("前往頁碼: ")
