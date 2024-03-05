#họ tên: Lê Anh Huy
#ngày thực hiện: 29/12/2023

def nhaptuoi(tuoi):
    if(tuoi > 18):
        print("Bạn đủ tuổi đi bầu!")
        if(tuoi > 100):
            print("Sao già dữ vậy!")
    else:
        print("Bạn chưa đủ tuổi đi bầu!")

tuoi = int(input("Bạn hãy nhập tuổi: "))
print("Tuổi của bạn là: ", tuoi)
nhaptuoi(tuoi)