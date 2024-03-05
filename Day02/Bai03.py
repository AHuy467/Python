#bài 1.4 tính hệ cơ số của n
#Lê Anh Huy
#05/01/2024

def convert_number(n,b):
    if (n<0 or b<2 or b>16):
        return ""
    sb = ""
    m = 0
    m = n
    while (m>0):
        if (b>10):
            m = m%b
            if (m>=10):
                sb = sb+str(chr(55+m))
            else:
                sb = sb+str(m)
        else:
            sb =sb+str(m%b)
        m = int(m/b)
    return "".join(reversed(sb)) #đảo ngược chuỗi sb

n = int(input("Nhập số nguyên dương n = "))
print("Hệ cơ số 2 của số nguyên ", n, "là: ", convert_number(n, 2))
print("Hệ cơ số 8 của số nguyên ", n, "là: ", convert_number(n, 8))
print("Hệ cơ số 16 của số nguyên ", n, "là: ", convert_number(n, 16))