#Bài 4
#Lê Anh Huy
#23/02/2024
#khởi tạo với các hàm có sẵn

import numpy as np
arr1 = np.zeros((3,4),dtype=int)
#Tạo mảng 2 chiều các phần tử 0 với kích thươc 3x4,
arr2 = np.zeros((2,3,4),dtype=int)
#Tạo mảng 3 chiều các phần tử 1 với kích thươc 2x3x4,
arr3 = np.arange(1,7,2)
#Tạo mảng với các phần tử từ 1-6 với bước nhảy là 2,
arr4 = np.full((2,3),5)
#Tạo mảng 2 chiều các phần tử 5 với kích thước 2x3.
arr5 = np.eye(4,dtype=int)
#Tạo ma trận đơn vị với kích thước 4x4.
arr6 = np.random.random((2,3))
#Tạo ma trận các phần tử ngẫu nhiên với kích thước 2x3.
print("Mảng 1: ")
print(arr1)
print("Mảng 2: ")
print(arr2)
print("Mảng 3: ")
print(arr3)
print("Mảng 4: ")
print(arr4)
print("Mảng 5: ")
print(arr5)
print("Mảng 6: ")
print(arr6)