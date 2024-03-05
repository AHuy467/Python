#Bài nhóm 9
#Lê Anh Huy - Nguyễn Hồng Ngọc
#
import numpy as np
import pandas as pd

# Đọc dữ liệu từ file CSV
data = pd.read_csv('democsv01.csv', delimiter=';')
# Hiển thị dữ liệu để kiểm tra
print("Dữ liệu từ file democsv01.csv:")
print(data)

#1 Số lượng mẫu tin
total_records = len(data)
print("1. Số lượng mẫu tin:", total_records)

#2 Tỉnh có nhiều sinh viên nhất
most_students_province = data.loc[data['SV'].idxmax()]
print("2. Tỉnh có nhiều sinh viên nhất:", most_students_province['Tinh'])

#3 Tỉnh có ít sinh viên nhất
least_students_province = data.loc[data['SV'].idxmin()]
print("3. Tỉnh có ít sinh viên nhất:", least_students_province['Tinh'])

#4 Tính trung bình
mean_students = np.mean(data['SV'])
print("4. Tính trung bình:", mean_students)

#5 Tính trung vị
median_students = np.median(data['SV'])
print("5. Tính trung vị:", median_students)

#6 Tính phương sai
variance_students = np.var(data['SV'])
print("6. Tính phương sai:", variance_students)

#7 Tính độ lệch chuẩn
std_dev_students = np.std(data['SV'])
print("7. Tính độ lệch chuẩn:", std_dev_students)

#8 Tính hệ số biến thiên (CV)
cv_students = (std_dev_students / mean_students) * 100
print("8. Tính hệ số biến thiên (CV):", cv_students)
