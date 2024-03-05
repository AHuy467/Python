#họ tên: Lê Anh Huy
#ngày thực hiện: 29/12/2023
import math
def Kiem_Tra_So_Nguyen_To(n):
    #So nguyen n < 2 khong phai la so nguyen to
    if (n < 2):
        return False;
    #Check so nguyen to khi n >= 2
    m = int(math.sqrt(n))
    for i in range(2, m + 1):
        if (n % i == 0):
            return False
    return True;

Danhsach = []
n = int(input("Bạn nhập vùng kiểm tra số nguyên tố: "))
print("Các số nguyên tố nhỏ hơn: ",n)
for i in range(0, n):
    if (Kiem_Tra_So_Nguyen_To(i)):
        Danhsach.append(i)
print(Danhsach)