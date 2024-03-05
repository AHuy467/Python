#Bài 6
#Lê Anh Huy
#23/02/2024
#Truy cập phần tử trong mảng

import numpy as np
arr2= np.array(([(2,4,0,6),(4,7,5,6)],
                [(0,3,2,1), (9,4,5,6)],
                [(5,8,6,4), (1,4,6,8)]), dtype = int)
print(arr2)
print("arr[2]=", arr2[2])
print("arr11[1:1]=", arr2[1:1])
print("arr2[1,2,3]=", arr2[1,1,3])
print("arr[0:3]=", arr2[0:3])
print("arr1[:,:1]=", arr2[:,:2])
