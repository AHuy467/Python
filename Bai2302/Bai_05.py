#Bài 5
#Lê Anh Huy
#23/02/2024
#Thao tác với mảng

import numpy as np
arr2= np.array(([(2,4,0,6),(4,7,5,6)],
                [(0,3,2,1), (9,4,5,6)],
                [(5,8,6,4), (1,4,6,8)]), dtype = int)
print(arr2)
print("Kiểu dữ liệu của phần tử trong mảng:", arr2.dtype)
print("Kích thước của mảng:", arr2.shape)
print("Số phần tử trong mảng:", arr2.size)
print("Số chiều của mảng:", arr2.ndim)