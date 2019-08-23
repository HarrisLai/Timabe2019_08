# x=["A","B","C"]
# print("".join(x))

# q=["","",""]
# q[0]=input("出生年")
# q[1]=input("出生月")
# q[2]=input("出生日")

# print("".join(q))
# print(" ".join(q))
# print("-".join(q))

# import sys
# print(sys.argv)
# print(sys.argv[0])
# print(sys.argv[1])

# import os
# a = os.system("dir")
#b = os.popen("dir")
#print(a)
#print(b)

# import sys as s
# import os

# if len(s.argv) == 2:
# 	os.system("dir "+s.argv[1]) #refer png
# else:
# 	print("input argv")

# import sys as s
# import os

# if len(s.argv) == 2:
# 	os.system("dir \""+s.argv[1]+"\"") #refer png
# else:
# 	print("input argv")

# import sys as s
# import os

# if len(s.argv) == 2:
# 	#os.system("dir \""+s.argv[1]+"\"") #refer png
# 	os.system("mkdir "+s.argv[1])
# 	os.system("dir")
# 	print("create folder")
# elif len(s.argv) == 3:
# 	os.system("rmdir "+s.argv[1])
# 	os.system("dir")
# 	print("remove folder")
# else:
# 	print("input argv")

import sys
import os

# #x="ABC\n123\nvb"
# p=os.popen("dir")
# #c = print(p.read()) #can read once only
# x=p.read().split("\n")
# print(x)
# print("END..........")
# print(x[len(x)-2].replace("   ",""))

#os.system("cd C:\\Program Files (x86)\\Google\\Chrome\\Application\\")
# three ways
#1. default OS call browser
#2. default call browser
#3. import modules



# import os

# a = "mkdir aa"
# b = os.popen(a,'r',1)
# print(b)

import codecs
import sys as s
import os

# p=codecs.open("test.txt","r","big5")
# #p.write("abhbfsdkjblndslnklfnlknv")
# print(p.read())
# #p.write("12344")
# p.close()

#os.remove("test.txt")
#os.rmdir("aaa")
# print(os.listdir("../"))

# for i in os.listdir("../"):
#  	if os.path.isdir("../"+i):
#  		print("目錄: ",i)
#  	else:
#  		print("檔案: ",i)

print(os.listdir("./"))

