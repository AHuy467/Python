#Pandas
#Lê Anh Huy
#26/01/2024

import pandas as pd
import os
import matplotlib.pyplot as ptl
df = pd.read_csv('Datafriend.csv')
# print(df)
# print(df['Noi Sinh'])
# print(set(df['Noi Sinh'])) #set là 1 tập hợp
# print(df.head(2)) #chỉ in 2 dòng kể từ đầu tiên
# print(df.shape) #đếm số dòng số cột trong file
print(df.shape)
df['Tuoi'] = [20,22,25,23,26] #Thêm 1 cột
df['Tuoi moi'] = df['Tuoi'] + 1 #Thêm 1 cột và cộng cột cũ lên 1
print(df)
print('Tuoi max: ', df['Tuoi moi'].max()) #Tuổi lớn nhất

#Lưu file csv
df.to_csv('Dulieu.csv')

noisinh_values=df.groupby('Noi Sinh').count()['Ho Ten']
print(noisinh_values)
noisinhs = ['TG','TP.HCM']
print(noisinhs)

ptl.bar(noisinhs, noisinh_values)
ptl.show()

