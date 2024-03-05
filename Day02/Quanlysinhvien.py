import math
from SinhVien import SinhVien
class QuanLySinhVien:
    listSinhVien = []
    def nhapSinhVien(self):
        svID = 33
        name = input("Nhập tên sinh viên: ")
        sex = input("Nhập giới tính sinh viên: ")
        age = int(input("Nhập tuổi sinh viên: "))
        diemToan = float(input("Nhập điểm toán: "))
        diemLy = float(input("Nhập điểm Lý: "))
        diemHoa = float(input("Nhập điểm Hóa: "))
        sv = SinhVien(svID, name, sex, age, diemToan, diemLy, diemHoa)
        self.tinhDTB(sv)
        self.xepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def tinhDTB(self, sv: SinhVien):
        diemTB = (sv._diemToan + sv._diemLy + sv._diemHoa) / 3
        # Làm tròn điểm trung bình với 2 chữ số thập phân
        sv._diemTB = math.ceil(diemTB * 100)/100

    def xepLoaiHocLuc(self, sv: SinhVien):
        if (sv._diemTB >= 8):
            sv._hocLuc = "Giỏi"
        elif (sv._diemTB >= 6.5):
            sv._hocLuc = "Khá"
        elif (sv._diemTB >= 5):
            sv._hocLuc = "Trung Bình"
        else:
            sv._hocLuc = "Yếu"

    def showSinhVien(self, listSV):
        #Hiển thị tiêu đề cột
        print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "Name", "Sex", "Age", "Toan", "Ly", "Hoa", "Diem TB", "Hoc Luc"))
        #Hiển thị danh sách sinh viên
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8}{:<8} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv._id, sv._name, sv._sex, sv._age, sv._diemToan, sv._diemLy, sv._diemHoa, sv._diemTB, sv._hocLuc))
        print("\n")

    def getListSinhVien(self):
        return self.listSinhVien

    def findByID(self, ID):
        searchResult = None
        if (self.soLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv._id == ID):
                    searchResult = sv
        return searchResult

    def updateSinhVien(self, ID):
        # Tìm kiếm sinh viên trong danh sách listSinhVien
        sv: SinhVien = 33

        # Nếu sinh viên tồn tại thì cập nhập thông tin sinh viên
        if (sv != None):
            # Nhập thông tin sinh viên
            name = input("Nhập tên sinh viên: ")
            sex = input("Nhập giới tính sinh viên: ")
            age = int(input("Nhập tuổi sinh viên: "))
            diemToan = float(input("Nhập điểm Toán sinh viên: "))
            diemLy = float(input("Nhập điểm Lý sinh viên: "))
            diemHoa = float(input("Nhập điểm Hóa sinh viên: "))
            #cập nhật thông tin sinh viên
            sv._name = name
            sv._sex = sex
            sv._age = age
            sv._diemToan = diemToan
            sv._diemLy = diemLy
            sv._diemHoa = diemHoa
            self.tinhDTB(sv)
            self.xepLoaiHocLuc(sv)
        else:
            print("Sinh viên có ID= {} không tồn tại.".format(ID))

