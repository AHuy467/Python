#Bài 10
#Lê Anh Huy
#23/02/2024
#Cho dữ liệu GDP : Dữ liệu tự tạo

#1. số mẫu tin
#2. GDP max
#3. GDP min
#4. Tính trung bình
#5. Tính trung vị
#6. Tính phương sai
#7. Tính độ lệch chuẩn
#8. Tính hệ số biến thiến(CV)
import numpy as np
import pandas as pd
data = pd.read_csv('gdp_lab.csv')
SoLuongMauTin = data.shape[0]
print("Số mẫu tin: ", SoLuongMauTin)

GDP_max = data['GDP (tỷ USD)'].max()
print("GDP tối đa: ", GDP_max)

GDP_min = data['GDP (tỷ USD)'].min()
print("GDP tối thiểu: ", GDP_min)

GDP_trung_binh = data['GDP (tỷ USD)'].mean()
print("GDP trung bình: ", GDP_trung_binh)

GDP_trung_vi = data['GDP (tỷ USD)'].median()
print("GDP trung vị: ", GDP_trung_vi)

GDP_phuong_sai = data['GDP (tỷ USD)'].var()
print("GDP phương sai: ", GDP_phuong_sai)

GDP_do_lech_chuan = data['GDP (tỷ USD)'].std()
print("GDP độ lệch chuẩn: ", GDP_do_lech_chuan)

CV = GDP_do_lech_chuan / GDP_trung_binh
print("Hệ số biến thiên (CV): ", CV)