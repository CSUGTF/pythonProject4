import studytest
filePath1=r'E:\D\data\210301-1'
filePath2=r'E:\D\data\210301-1.xlsx'
aimpath='E:\D\data\\test'
dirs=studytest.Find_File_Name(filePath1)
studytest.excel_devide(filePath2,dirs,aimpath)