import numpy as np
import csv
import pandas as pd
import os
import xlrd
#读取csv文件方式
#csvFile = pd.read_excel(r'C:\D\1\210301-1.xlsx')

#查找文件夹里各文件夹名字
filePath=r'E:\D\data\210301-1'
a=[]
for root,dirs,files in os.walk(filePath,topdown=False):
   print(root)
   print(dirs)
   for file in files:
      a.append(file)
   print(files)
print(a)
print(type(dirs[0]))

#读取excel表格
#data=pd.read_excel(r'E:\D\data\test.xlsx')
#data.to_excel(r'E:\D\data\new.xlsx')




#c=r'E:\D\data'
#b = os.listdir(c)
#print(b)





