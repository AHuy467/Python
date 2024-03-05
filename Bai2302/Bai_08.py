#Bài 8
#Lê Anh Huy
#23/02/2024
#Hàm thống kê

import numpy as np
diem = np.loadtxt('Diem.txt', dtype = int, delimiter=',')
#các phần từ phân tách nhau bởi dấu ","
print("File dữ liệu điểm lớp :\n, diem")
print("Giá trị lớn nhất của mảng arr là:", np.max(diem))
print("Giá trị nhỏ nhất của mảng arr là:", np.min(diem))
print("Tổng các phần tử của của mảng arr là:", np.max(diem))
print("Trung bình cộng tất cả các phần tử của mảng arr là:", np.mean(diem))
print("Giá trị trung vị của mảng arr là:", np.median(diem))
