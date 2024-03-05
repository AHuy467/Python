#Bài 7
#Lê Anh Huy
#23/02/2024
#Đọc mảng từ file .txt

import numpy as np
diem = np.loadtxt('Diem.txt', dtype = int, delimiter=',')
#Các phần tử phân tách nhau bơ dấu ","
print("File dữ liệu điểmm lớp:\n", diem)
arr=diem.reshape(3,10)
print("File dữ liệu điểm tuần:\n", arr)