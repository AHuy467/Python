#Đồ án nhóm 9 - Phân tích đánh giá số ca tử vong và số ca nhiễm do COVID 19 Từ năm 2020 - 2022
#Thầy Trương Bá Thái
#Lê Anh Huy - 2200118191
#Nguyên Hồng Ngọc - 2200115650
#15/03/2024

#1. Số lượng mẫu tin của tất cả các năm

#2. Đọc thông tin vào tạo biểu đồ từng tháng các năm 2020, 2021, 2022
#3. Thống kê tổng số ca tử vong và số ca nhiễm và khỏi của từng năm
#4. Thống kê tháng có số ca nhiễm và ca tử vong và khỏi cao nhất của từng năm
#6. Thống kê năm có số ca tử vong và ca nhiễm và khỏi thấp nhất qua từng năm
#7. Xuất ra số ca nhiễm và ca tử vong tính theo quý của từng năm

#8. So sánh và đánh giá tăng giảm của các thống kê trên // word

#10. Hiển thị biểu đồ dữ liệu so sánh số ca nhiễm và tử vong từng quý
#11. Hiển thị biểu đồ dữ liệu số ca nhiễm theo

#12. Đường xu hướng (tìm hiểu) dùng đường xu hướng tuyến tính (Đã xong)

#14. Tính trung vị
#15. Tính phương sai

#16. Tính trung bình

#17. Tính độ lệch chuẩn
#18. Tính hệ số biến thiến(CV)

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

# Đọc dữ liệu từ file CSV
df = pd.read_csv("CovidNhom9_2020_2021_2022.csv", delimiter=";")
num_samples = len(df)

# Tạo hình vẽ cho năm 2020 và 2021
fig, axs_2020_2021 = plt.subplots(1, 2, figsize=(15, 5))

# Biểu đồ năm 2020 và 2021
axs_2020_2021[0].plot(df['Tháng'], df['Số ca nhiễm 2020'], label='Nhiễm', marker='o')
axs_2020_2021[0].plot(df['Tháng'], df['Số ca tử vong 2020'], label='Tử vong', marker='o')
axs_2020_2021[0].plot(df['Tháng'], df['Số ca khỏi 2020'], label='Khỏi', marker='o')
axs_2020_2021[0].set_title('Dữ liệu năm 2020')
axs_2020_2021[0].legend()

axs_2020_2021[1].plot(df['Tháng'], df['Số ca nhiễm 2021'], label='Nhiễm', marker='o')
axs_2020_2021[1].plot(df['Tháng'], df['Số ca tử vong 2021'], label='Tử vong', marker='o')
axs_2020_2021[1].plot(df['Tháng'], df['Số ca khỏi 2021'], label='Khỏi', marker='o')
axs_2020_2021[1].set_title('Dữ liệu năm 2021')
axs_2020_2021[1].legend()

# Tạo hình vẽ cho năm 2021 và 2022
fig, axs_2021_2022 = plt.subplots(1, 2, figsize=(15, 5))

# Biểu đồ năm 2021 và 2022
axs_2021_2022[0].plot(df['Tháng'], df['Số ca nhiễm 2021'], label='Nhiễm', marker='o')
axs_2021_2022[0].plot(df['Tháng'], df['Số ca tử vong 2021'], label='Tử vong', marker='o')
axs_2021_2022[0].plot(df['Tháng'], df['Số ca khỏi 2021'], label='Khỏi', marker='o')
axs_2021_2022[0].set_title('Dữ liệu năm 2021')
axs_2021_2022[0].legend()

axs_2021_2022[1].plot(df['Tháng'], df['Số ca nhiễm 2022'], label='Nhiễm', marker='o')
axs_2021_2022[1].plot(df['Tháng'], df['Số ca tử vong 2022'], label='Tử vong', marker='o')
axs_2021_2022[1].plot(df['Tháng'], df['Số ca khỏi 2022'], label='Khỏi', marker='o')
axs_2021_2022[1].set_title('Dữ liệu năm 2022')
axs_2021_2022[1].legend()

plt.suptitle(f"Số lượng mẫu: {num_samples}")
plt.show()

# Đọc dữ liệu từ file CSV
df = pd.read_csv("CovidNhom9_2020_2021_2022.csv", delimiter=";")

# Chuyển đổi cột Tháng thành index
df.set_index("Tháng", inplace=True)

#7. Xuất ra số ca nhiễm và ca tử vong tính theo quý của từng năm
df["Quý"] = pd.cut(df.index, bins=[0, 3, 6, 9, 12], labels=["Quý 1", "Quý 2", "Quý 3", "Quý 4"])

cases_deaths_by_quarter_2020 = df.groupby("Quý", observed=True)[['Số ca nhiễm 2020', 'Số ca tử vong 2020']].sum()
cases_deaths_by_quarter_2021 = df.groupby("Quý", observed=True)[['Số ca nhiễm 2021', 'Số ca tử vong 2021']].sum()
cases_deaths_by_quarter_2022 = df.groupby("Quý", observed=True)[['Số ca nhiễm 2022', 'Số ca tử vong 2022']].sum()

print("Số ca nhiễm và ca tử vong tính theo quý của năm 2020:")
print(cases_deaths_by_quarter_2020)
print("\nSố ca nhiễm và ca tử vong tính theo quý của năm 2021:")
print(cases_deaths_by_quarter_2021)
print("\nSố ca nhiễm và ca tử vong tính theo quý của năm 2022:")
print(cases_deaths_by_quarter_2022)
print("")

# Xuất ra số ca nhiễm và số ca tử vong lớn nhất của từng năm
max_cases_deaths_2020 = df[['Số ca nhiễm 2020', 'Số ca tử vong 2020']].max().to_string()
max_cases_deaths_2021 = df[['Số ca nhiễm 2021', 'Số ca tử vong 2021']].max().to_string()
max_cases_deaths_2022 = df[['Số ca nhiễm 2022', 'Số ca tử vong 2022']].max().to_string()

print("------Số ca nhiễm và số ca tử vong lớn nhất------")
print("Số ca nhiễm và số ca tử vong lớn nhất của năm 2020:")
print(max_cases_deaths_2020)
print("\nSố ca nhiễm và số ca tử vong lớn nhất của năm 2021:")
print(max_cases_deaths_2021)
print("\nSố ca nhiễm và số ca tử vong lớn nhất của năm 2022:")
print(max_cases_deaths_2022)
print("")

# Xuất ra số ca nhiễm và số ca tử vong thấp nhất của từng năm
min_cases_deaths_2020 = df[['Số ca nhiễm 2020', 'Số ca tử vong 2020']].min().to_string()
min_cases_deaths_2021 = df[['Số ca nhiễm 2021', 'Số ca tử vong 2021']].min().to_string()
min_cases_deaths_2022 = df[['Số ca nhiễm 2022', 'Số ca tử vong 2022']].min().to_string()

print("------Số ca nhiễm và số ca tử vong thấp nhất------")
print("Số ca nhiễm và số ca tử vong nhỏ nhất của năm 2020:")
print(min_cases_deaths_2020)
print("\nSố ca nhiễm và số ca tử vong nhỏ nhất của năm 2021:")
print(min_cases_deaths_2021)
print("\nSố ca nhiễm và số ca tử vong nhỏ nhất của năm 2022:")
print(min_cases_deaths_2022)
print("")

# Biểu đồ số ca nhiễm theo từng năm
# Đọc dữ liệu từ file CSV
df = pd.read_csv("CovidNhom9_2020_2021_2022.csv", delimiter=';')

# Tạo biểu đồ
plt.figure(figsize=(10, 6))

# Vẽ dữ liệu từng năm
plt.plot(df['Tháng'], df['Số ca nhiễm 2020'] / 1000, label='2020', marker='o')
plt.plot(df['Tháng'], df['Số ca nhiễm 2021'] / 1000, label='2021', marker='o')
plt.plot(df['Tháng'], df['Số ca nhiễm 2022'] / 1000, label='2022', marker='o')

# Thiết lập tiêu đề và nhãn cho trục x và y
plt.title('Số ca nhiễm Covid-19 từ 2020 đến 2022')
plt.xlabel('Tháng')
plt.ylabel('Số ca nhiễm (nghìn)')
plt.xticks(df['Tháng'])  # Đảm bảo hiển thị tất cả các tháng trên trục x
plt.grid(True)

# Định dạng số trên trục y theo hàng nghìn
plt.ticklabel_format(style='plain', axis='y')
plt.gca().get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))

# Hiển thị chú thích
plt.legend()

# Hiển thị biểu đồ
plt.show()

#ĐƯỜNG XU HƯỚNG
# Đọc dữ liệu từ tệp CSV vào một DataFrame
df = pd.read_csv("CovidNhom9_2020_2021_2022.csv", delimiter=";")

# Tạo mảng chứa tháng
months = df['Tháng']

# Tạo mảng chứa các số liệu cần theo dõi cho các năm
data_2020 = df['Số ca nhiễm 2020'].values
data_2021 = df['Số ca nhiễm 2021'].values
data_2022 = df['Số ca nhiễm 2022'].values

# Tính số lượng tháng
n_months = len(months)

# Tạo mảng chứa các giá trị x (tháng)
x_values = np.arange(1, n_months + 1)

# Thực hiện hồi quy tuyến tính cho mỗi năm (linregress dùng để tính hệ số góc và điểm cắt, hàm này xuất từ thư viện scipy.stats)
slope_2020, intercept_2020, _, _, _ = linregress(x_values, data_2020)
slope_2021, intercept_2021, _, _, _ = linregress(x_values, data_2021)
slope_2022, intercept_2022, _, _, _ = linregress(x_values, data_2022)

# Tạo đường xu hướng cho mỗi năm
trend_line_2020 = slope_2020 * x_values + intercept_2020
trend_line_2021 = slope_2021 * x_values + intercept_2021
trend_line_2022 = slope_2022 * x_values + intercept_2022

# Vẽ biểu đồ
fig, axs = plt.subplots(3, 1, figsize=(10, 18))

# Biểu đồ năm 2020
axs[0].plot(months, data_2020, marker='o', label='2020')
axs[0].plot(months, trend_line_2020, '--', label='Đường xu hướng 2020')
axs[0].set_title('Đường xu hướng số ca nhiễm Covid-19 năm 2020')
axs[0].set_xlabel('')
axs[0].set_ylabel('Số ca nhiễm')
axs[0].legend()
axs[0].grid(True)

# Biểu đồ năm 2021
axs[1].plot(months, data_2021, marker='o', label='2021')
axs[1].plot(months, trend_line_2021, '--', label='Đường xu hướng 2021')
axs[1].set_title('năm 2021')
axs[1].set_xlabel('')
axs[1].set_ylabel('Số ca nhiễm')
axs[1].legend()
axs[1].grid(True)

# Biểu đồ năm 2022
axs[2].plot(months, data_2022, marker='o', label='2022')
axs[2].plot(months, trend_line_2022, '--', label='Đường xu hướng 2022')
axs[2].set_title('năm 2022')
axs[2].set_xlabel('Tháng')
axs[2].set_ylabel('Số ca nhiễm')
axs[2].legend()
axs[2].grid(True)

plt.tight_layout()
plt.show()

#Tính trung vị số ca nhiễm
# Đọc dữ liệu từ tệp CSV vào một DataFrame
df = pd.read_csv("CovidNhom9_2020_2021_2022.csv", delimiter=";")

# Lấy cột chứa số ca nhiễm 2020, 2021 và 2022
cases_2020 = df['Số ca nhiễm 2020']
cases_2021 = df['Số ca nhiễm 2021']
cases_2022 = df['Số ca nhiễm 2022']

# Tính trung vị cho mỗi năm
median_cases_2020 = cases_2020.median()
median_cases_2021 = cases_2021.median()
median_cases_2022 = cases_2022.median()

# Làm tròn trung vị (round là hàm làm tròn của thư viện numpy)
rounded_median_cases_2020 = round(median_cases_2020)
rounded_median_cases_2021 = round(median_cases_2021)
rounded_median_cases_2022 = round(median_cases_2022)

print("------Trung vị số ca nhiễm Covid-19------")
print("Trung vị số ca nhiễm Covid-19 năm 2020:", rounded_median_cases_2020)
print("Trung vị số ca nhiễm Covid-19 năm 2021:", rounded_median_cases_2021)
print("Trung vị số ca nhiễm Covid-19 năm 2022:", rounded_median_cases_2022)
print("")

#TÍNH PHƯƠNG SAI SỐ CA NHIỄM
# Đọc dữ liệu từ tệp CSV vào một DataFrame
df = pd.read_csv("CovidNhom9_2020_2021_2022.csv", delimiter=";")

# Tính phương sai cho mỗi năm
variance_cases_2020 = np.var(cases_2020)
variance_cases_2021 = np.var(cases_2021)
variance_cases_2022 = np.var(cases_2022)

# Làm tròn phương sai
rounded_variance_cases_2020 = round(variance_cases_2020, 2)
rounded_variance_cases_2021 = round(variance_cases_2021, 2)
rounded_variance_cases_2022 = round(variance_cases_2022, 2)

print("------Phương sai số ca nhiễm Covid-19------")
print("Phương sai số ca nhiễm Covid-19 năm 2020:", rounded_variance_cases_2020)
print("Phương sai số ca nhiễm Covid-19 năm 2021:", rounded_variance_cases_2021)
print("Phương sai số ca nhiễm Covid-19 năm 2022:", rounded_variance_cases_2022)
print("")

#TÍNH TRUNG BÌNH SỐ CA NHIỄM
# Đọc dữ liệu từ tệp CSV vào một DataFrame
df = pd.read_csv("CovidNhom9_2020_2021_2022.csv", delimiter=";")

# Tính trung bình cho mỗi năm
mean_cases_2020 = np.mean(cases_2020)
mean_cases_2021 = np.mean(cases_2021)
mean_cases_2022 = np.mean(cases_2022)

# Làm tròn trung bình
rounded_mean_cases_2020 = round(mean_cases_2020)
rounded_mean_cases_2021 = round(mean_cases_2021)
rounded_mean_cases_2022 = round(mean_cases_2022)

print("------Trung bình số ca nhiễm Covid-19------")
print("Trung bình số ca nhiễm Covid-19 năm 2020:", rounded_mean_cases_2020)
print("Trung bình số ca nhiễm Covid-19 năm 2021:", rounded_mean_cases_2021)
print("Trung bình số ca nhiễm Covid-19 năm 2022:", rounded_mean_cases_2022)
print("")

#TÍNH ĐỘ LỆCH CHUẨN CHO MỖI NĂM
# Đọc dữ liệu từ tệp CSV vào một DataFrame
df = pd.read_csv("CovidNhom9_2020_2021_2022.csv", delimiter=";")

# Tính độ lệch chuẩn cho mỗi năm
std_cases_2020 = np.std(cases_2020)
std_cases_2021 = np.std(cases_2021)
std_cases_2022 = np.std(cases_2022)

# Làm tròn độ lệch chuẩn
rounded_std_cases_2020 = round(std_cases_2020, 2)
rounded_std_cases_2021 = round(std_cases_2021, 2)
rounded_std_cases_2022 = round(std_cases_2022, 2)

print("------Độ lệch chuẩn số ca nhiễm Covid-19------")
print("Độ lệch chuẩn số ca nhiễm Covid-19 năm 2020:", rounded_std_cases_2020)
print("Độ lệch chuẩn số ca nhiễm Covid-19 năm 2021:", rounded_std_cases_2021)
print("Độ lệch chuẩn số ca nhiễm Covid-19 năm 2022:", rounded_std_cases_2022)
print("")

#TÍNH HỆ SỐ BIẾN THIÊN
#CÔNG THỨC NHƯ SAU:
#     Hệ số biến thiên = Độ lệch chuẩn / Trung bình

# Tính hệ số biến thiên cho mỗi năm
coefficient_of_variation_2020 = std_cases_2020 / mean_cases_2020
coefficient_of_variation_2021 = std_cases_2021 / mean_cases_2021
coefficient_of_variation_2022 = std_cases_2022 / mean_cases_2022

# Làm tròn hệ số biến thiên
rounded_coefficient_of_variation_2020 = round(coefficient_of_variation_2020, 2)
rounded_coefficient_of_variation_2021 = round(coefficient_of_variation_2021, 2)
rounded_coefficient_of_variation_2022 = round(coefficient_of_variation_2022, 2)

print("------Hệ số biến thiên số ca nhiễm Covid-19------")
print("Hệ số biến thiên số ca nhiễm Covid-19 năm 2020:", rounded_coefficient_of_variation_2020)
print("Hệ số biến thiên số ca nhiễm Covid-19 năm 2021:", rounded_coefficient_of_variation_2021)
print("Hệ số biến thiên số ca nhiễm Covid-19 năm 2022:", rounded_coefficient_of_variation_2022)
print("")