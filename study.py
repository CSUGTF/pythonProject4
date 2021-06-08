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
#print(type(dirs[1]))


#读取excel表格
data=pd.read_excel(r'E:\D\data\210301-1.xlsx')
#print(data.loc[2])
#查找data中有动态数据的组
dirs_count=0            # dirs_count初始化
data_new=data.loc[0:1]  # data_new 初始化
old_data=0
count=0
for dirs_num in dirs:
   list = []
   if count>0:
      while old_data>=-1:
         data_new.drop(0,axis=0,inplace=True) # 删除data_new第一行数据
         data_new.reset_index(drop=True, inplace=True) #重排index
         old_data-=1
      old_data=0
      data_new=data_new.append(data.loc[0:1])  #接个头
   count=0                 # count初始化
   for flag1 in data.loc[2:,'Tray ID']:
      count+=1
      if dirs_num in flag1[-4:]:  # flag1[-4:] 选取从倒数第四个字符到最后的字符
         #print(data.index[count])
         list.append(count)
         old_data+=1
      #print(flag1)
      #print(list)

    # 将有动态数据的组提取出来存入新的xlsx组内
   for index_new in list:
      data_new=data_new.append(data.loc[index_new+1],ignore_index=True)

   a=dirs[dirs_count]
   print(a)
   data_new.to_excel('E:\D\data\\test\{add1}\{add2}-静态数据.xlsx'.format(add1=str(a),add2=str(a)))
   dirs_count+=1




#c=r'E:\D\data'
#b = os.listdir(c)
#print(b)





