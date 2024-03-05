#họ tên: Lê Anh Huy
#ngày thực hiện: 29/12/2023

import math
#Hàm giải PTB2
def ptb2(a, b, c):
    if a == 0:
        if b == 0:
            if c == 0:
                print("Phương trình vô số nghiệm")
            else:
                print("Phương trình vô nghiệm")
        else:
            print("Phương trình có nghiệm", (-c / b))
    else:
        delta = b * b - 4 * a * c
        if delta > 0:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            print("Phương trình có 2 nghiệm phân biệt")
            print("Nghiệm x1 :", x1)
            print("Nghiệm x2 :", x2)
        elif delta == 0:
            x = -b / (2 * a)
            print("Phương trình có nghiệm kép x1 = x2 =", x)
        else:
            print("Phương trình vô nghiệm")

# Nhập các hệ số từ người dùng và gọi hàm giải phương trình
a = float(input("Nhập số a: "))
b = float(input("Nhập số b: "))
c = float(input("Nhập số c: "))

ptb2(a, b, c)

# a = 0 bậc 1
# 121 nghiệm kép (a=c)
# 234 - 567 vô nghiệm
# 1-32 phân biệt (có 1 số âm)
# 000 vô số nghiệm