from Quanlysinhvien import QuanLySinhVien
qlsv = QuanLySinhVien()
qlsv.nhapSinhVien()
qlsv.showSinhVien(qlsv.getListSinhVien())
print("\nCập nhật thông tin: ")
qlsv.updateSinhVien(33)
qlsv.showSinhVien(qlsv.getListSinhVien())