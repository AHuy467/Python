#Tính giai thừa của một số
#Lê Anh Huy
#05/01/2024

def tinhgiaithua(n):
    giai_thua = 1
    if (n==0 or n==1):
        print(f"{n}! = 1")
        return giai_thua
    else:
        for i in range(2, n+1):
            giai_thua = giai_thua*i
            print(f"{n}! = ", end="")
            for i in range(1,n):
                print(f"{i} * ", end="")
            print(f"{n} = {tinhgiaithua(n)}")

        return giai_thua

n = int(input("Nhap so nguyen duong n = "))
print("Giai thừa cua",n," là ", tinhgiaithua(n))

