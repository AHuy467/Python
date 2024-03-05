#Pandas
#Lê Anh Huy
#26/01/2024

import  pandas as pd
import os
import  matplotlib.pyplot as plt


frames=[]
path='E:\\VanLang\\Python\\Data'
for file in os.listdir(path):
    print(file)
    if(file.endswith('.csv')):
        filename= path+"\\"+file
        print(filename)
        df=pd.read_csv(filename)
        frames.append(df)
    df=pd.concat(frames)

#them cot thang
df['Month']=df['Order Date'].str[0:2]
print(set(df['Month']))

#lam sach du lieu
df=df.dropna()
df=df[df['Month']!='Or']
print(set(df['Month']))
print(df)

#bao cao
#chuyen doi kieu du lieu
df['Quantity Ordered']=pd.to_numeric(df['Quantity Ordered'],downcast='integer')
df['Price Each']=pd.to_numeric(df['Price Each'],downcast='float')

#tinh thanh tien
df['Sales']=df['Quantity Ordered']*df['Price Each']

#tinh tong tien theo thang ( thong ke )
sales_values=df.groupby('Month').sum()['Sales']
print(sales_values)

#bieu do
Months=[]
for Month, Sales in sales_values.items():
    Months.append(Month)
plt.bar(Months,sales_values)
plt.xlabel('Thang')
plt.ylabel('Tong tien')
plt.title('Thong ke')
plt.show()

#Thống kê những cửa hàng có doanh thu cao nhất trong năm, In tên thành phố của những cửa hàng đó
#Gợi ý lấy từ "Purchase Address"
# Thống kê những cửa hàng có doanh thu cao nhất trong năm
city_sales = df.groupby('Purchase Address')['Sales'].sum()

# Lấy thông tin về cửa hàng có doanh thu cao nhất
highest_revenue_stores = city_sales.nlargest(5)  # Lấy 5 cửa hàng có doanh thu cao nhất
print("Các cửa hàng có doanh thu cao nhất trong năm:")
for store, revenue in highest_revenue_stores.items():
    print(f"Cửa hàng: {store}, Doanh thu: {revenue}")

# Vẽ biểu đồ cho thông tin cửa hàng có doanh thu cao nhất
plt.figure(figsize=(10, 6))
plt.bar(highest_revenue_stores.index, highest_revenue_stores.values)
plt.xlabel("Cửa hàng")
plt.ylabel("Doanh thu")
plt.title("Các cửa hàng có doanh thu cao nhất trong năm")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Xuất dữ liệu đã xử lý ra file CSV
df.to_csv('ThongKeKinhDoanh.csv', index=False)