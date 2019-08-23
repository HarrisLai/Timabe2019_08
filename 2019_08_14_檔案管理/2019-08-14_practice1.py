# str="-"
# seq=["a","b","c","d"]

# a=str.join(seq)
# print("str: ",str)
# print("a: ", a)

# import sys as test
# #a = sys.argv
# a = test.argv
# print(a)

import os
#os.system("cmd")
#print(os.system("mkdir test"))
#os.system("mkdir test")
a = os.popen("cmd")
print(a)
