import requests
import codecs
import csv
import io
import prettytable

#==============HW1===========
# p=requests.get(
# 	"http://data.coa.gov.tw/Service/OpenData/ODwsv/ODwsvTravelFood.aspx?FOTT=CSV"
# 	#"https://gis.taiwan.net.tw/od/01_PRD/歷年來台旅客統計.csv"
# )
# p.encoding="utf8"
# #print(p.text)
# #f=io.StringIO(p.text)

# #f=io.StringIO(["AA","BB","CC"])

# #open with sublime and the save as csv again, the format is correct now
# f=codecs.open("COA_OpenData.csv","r","utf8")
# result=list(csv.reader(f))
# print(result)

#=========================HW2=====================================
# p=requests.get(
# 	"https://gis.taiwan.net.tw/od/01_PRD/歷年來台旅客統計.csv"
# )
# #p.encoding="utf8"
# p.encoding="big5"

# f=io.StringIO(p.text)
# result=list(csv.reader(f))

# w=prettytable.PrettyTable(result[0],encoding="big5")
# for i in result[1:]:
# 	w.add_row(i)

# print(w)	

# s=codecs.open("result.txt","w")
# s.write(str(w))
# s.close()
# ==============================================

#test
# p=requests.get(
# 	"https://gis.taiwan.net.tw/od/01_PRD/歷年來台旅客統計.csv"
# )
# #p.encoding="utf8"
# p.encoding="big5"

# #print(result=list(csv.reader(p.text)))
# #print(p.text)
# print(list(csv.reader(p.text)))
# # f=io.StringIO(p.text)
# # result=list(csv.reader(f))
# # print(result)
# w=prettytable.PrettyTable(result[0],encoding="big5")
# for i in result[1:]:
# 	w.add_row(i)

# print(w)	

# s=codecs.open("result.txt","w")
# s.write(str(w))
# s.close()
# # ==============================================
import json
p=requests.get(
	#"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/E-A0073-001?Authorization=rdec-key-123-45678-011121314&format=JSON"
	"https://data.tycg.gov.tw/opendata/datalist/datasetMeta/download?id=f4cc0b12-86ac-40f9-8745-885bddc18f79&rid=0daad6e6-0632-44f5-bd25-5e1de1e9146f"
)
p.encoding="utf8"
#p.encoding="big5"

#print(p.text)

j=json.loads(p.text) #from json to dictionary
print(j)
# for i in j["parkingLots"]:
# 	print(i["areaName"],":",i["parkName"])
# 	#print(i,":",i)

#ps: if 被擋, 再請求區填入head

# print(list(csv.reader(p.text)))
# # f=io.StringIO(p.text)
# # result=list(csv.reader(f))
# # print(result)
# w=prettytable.PrettyTable(result[0],encoding="big5")
# for i in result[1:]:
# 	w.add_row(i)

# print(w)	

# s=codecs.open("result.txt","w")
# s.write(str(w))
# s.close()

# for d in j["frt"].items(): #for dictionary only
# or using 
# for k,d in j["frt"].items():