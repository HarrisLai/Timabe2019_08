import os
import sys as sys

print("Working Director: ", os.getcwd())
y={
"(0)":"離開程式",
"(1)":"列出檔案",
"(2)":"列出資料夾",
"(3)":"檔案內容",
"(4)":"刪除檔案",
"(5)":"執行檔案",
"(6)":"進入資料夾",
"(7)":"刪除資料夾",
"(8)":"回上一層資料夾"
}
for k,v in y.items():
	print(k,v)

get=input("\n操作:")
number=int(get)
print(number)
if number==0:
	exit()
elif number==1:
	print("list files")
elif number==2:
	print("list folders")
elif number==3:
	print("files content")
elif number==4:
	print("delete")
elif number==5:
	print("run")
elif number==6:
	print("enter folders")
elif number==7:
	print("delete folders")
elif number==8:
	print("upper folder")

print("END...........")
