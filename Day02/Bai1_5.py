#bài 1.5 Liệt kê các số nguyên tố nhỏ hơn fibanacci
#Lê Anh Huy
#05/01/2024
import math
def fibonacci(n):
    if(n<0):
        return -1
    elif (n==0 or n ==1):
        return n
    else:
        return fibonacci(n - 1)+ fibonacci(n-2)
def isPirmeNumber(n):
    #so nguyen n< 2 khong phai la so nguyen to
    if(n<2):
        return False;
    #check so nguyen to khi n>=2
    squareRoot = int(math.sqrt(n))
    for i in range(2, squareRoot+1):
        if (n%i==0):
            return False
    return True

n = int(input("Nhap so nguyen duong n = "))
print("Tat ca cac so Fibonacci nho hon", n, "va nguyen to: ")
i = 0
fin = fibonacci(i)
while (fin<n):
    fin = fibonacci(i)
    if(isPirmeNumber(fin)):
        print(fin)
    i+=1
