import pandas as pd

# Đọc dữ liệu
df = pd.read_csv("democsv02.csv")

# Số lượng mẫu tin
so_luong_mau_tin = len(df)

print("Số lượng mẫu tin:", so_luong_mau_tin)

# Tỉnh ít sinh viên nhất
tinh_it_sinh_vien_nhat = df.groupby("Tinh").size().sort_values(ascending=True).index[0]

print("Tỉnh ít sinh viên nhất:", tinh_it_sinh_vien_nhat)
