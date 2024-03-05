#Đọc file excel
#Lê Anh Huy
#19/01/2024

# import pandas as pd
#
# #  Đọc file CSV, đường dẫn tới file CSV
# thongtin = pd.read_csv('E:\VanLang\Python\Baikt.csv')
#
# # In ra nội dung của DataFrame
# print(thongtin.head())

import csv

# Đường dẫn tới file CSV
Baikt = 'Baikt.csv'

# Mở file CSV và đọc dữ liệu
with open(Baikt, 'r') as file:
    # Sử dụng DictReader để đọc dữ liệu và chuyển thành từ điển
    Doc = csv.DictReader(file)

    # In ra tên các cột (header)
    print(Doc.fieldnames)

    # In ra dữ liệu từ mỗi hàng
    for row in Doc:
        print(row)
