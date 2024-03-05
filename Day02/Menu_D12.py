# from .B1_NhapTuoi import nhaptuoi
# from .B2_PTB2 import ptb2
# from .B1_NhapTuoi import nhaptuoi
# from .B1_NhapTuoi import nhaptuoi
# from .B1_NhapTuoi import nhaptuoi
# from .B1_NhapTuoi import nhaptuoi
# from .B1_NhapTuoi import nhaptuoi

# def menu1():
#     nhaptuoi()
# def menu2():
#
# def menu3():
# def menu4():
# def menu5():
# def menu6():
# def menu7():

while True:
    print("\n Chương trình bài tập cơ bản")
    print("******************** - MENU - ******************")
    print("**   1. Nhập tuổi                             **")
    print("**   2. Tính phương trình bậc 2               **")
    print("**   3. Liệt kê các số nguyên tố < Fibonacci  **")
    print("**   4. Tính giai thừa                        **")
    print("**   5. Tính hệ cơ số của n                   **")
    print("**   6. Kiểm tra số nguyên tố n               **")
    print("**   7. Thừa số nguyên tố                     **")
    print("**   --------------------                     **")
    print("**   0. Thoát                                 **")

    key = input("Vui lòng chọn chức năng: ")
    if key == "1":
        print("**   1. Nhập tuổi                             **")
        import B1_NhapTuoi
    elif key == "2":
        print("**   2. Tính phương trình bậc 2               **")
        import B2_PTB2
    elif key == "3":
        print("**   3. Liệt kê các số nguyên tố < Fibonacci  **")
        import Bai1_5
    elif key == "4":
        print("**   4. Tính giai thừa                        **")
        import Bai01
    elif key == "5":
        print("**   5. Tính hệ cơ số của n                   **")
        import Bai03
    elif key == "6":
        print("**   6. Kiểm tra số nguyên tố n               **")
        import KTSoNguyenTo
    elif key == "7":
        print("**   7. Thừa số nguyên tố                     **")
        import ThuasoNguyento
    else:
        print("Chọn lại đi")

import subprocess

# while True:
#     print("\n CHƯƠNG TRÌNH BÀI TẬP CƠ BẢN")
#     print("*****************************************************")
#     print("** 1. tính tuổi .                                    ")
#     print("** 2. Phương trình bậc 2.                            ")
#     print("** 3. Kiểm tra số nguyên tố.                         ")
#     print("** 4. Tính giai thừa.                                ")
#     print("** 5. Phân tích số nguyên.                           ")
#     print("** 6. fibonacci.                                     ")
#     print("** 7. Chuyển đổi số.                                 ")
#     print("** 0. Thoát chương trình.                            ")
#     print("*****************************************************")
#     key = int(input("Nhập tùy chọn: "))
#     if key == 1:
#         subprocess.run(['python', 'bài 1.py'])
#     elif key == 2:
#         subprocess.run(['python', 'bài 2.py'])
#     elif key == 3:
#         subprocess.run(['python', 'bài 3.py'])
#     elif key == 4:
#         subprocess.run(['python', 'bài 4.py'])
#     elif key == 5:
#         subprocess.run(['python', 'bài 5.py'])
#     elif key == 6:
#         subprocess.run(['python', 'bài 6.py'])
#     elif key == 7:
#         subprocess.run(['python', 'bài 7.py'])
#     elif key == 0:
#         print("Thoát chương trình.")
#         break
#     else:
#         print("Tùy chọn không hợp lệ. Vui lòng thử lại.")