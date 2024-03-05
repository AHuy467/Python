#bài 1.4 tính hệ cơ số của n 10 = 2^5
#Lê Anh Huy
#05/01/2024

import math
# def phanTichSoNguyen(n):
#     i = 2
#     listNumbers = []
#     while (n > 1):
#         if (n % i == 0):
#             n = int(n / i)
#             listNumbers.append(i)
#         else:
#             i = i + 1
#     if (len(listNumbers) == 0):
#         listNumbers.append(n)
#     return listNumbers
# n = int(input("Nhập số nguyên dương n = "))
# listNumbers = phanTichSoNguyen(n)
# size = len(listNumbers)
# sb = ""
# for i in range(0, size - 1):
#     sb = sb + str(listNumbers[i]) + " x "
# sb = sb + str(listNumbers[size - 1])
# print("Kết quả:", n, "=", sb)

# def phanTichSoNguyen(n):
#     i = 2
#     listNumbers = []
#     while (n > 1):
#         if (n % i == 0):
#             n = int(n / i)
#             listNumbers.append(i)
#         else:
#             i = i + 1
#     if (len(listNumbers) == 0):
#         listNumbers.append(n)
#     return listNumbers
#
# n = int(input("Nhập số nguyên dương n = "))
# listNumbers = phanTichSoNguyen(n)
#
# result = ""
# for num in listNumbers:
#     result += f"2^{num} * "
#
# result = result[:-3]  # Remove the extra ' * ' at the end
# print("Kết quả:", n, "=", result)


def phanTichSoNguyen(n):
    i = 2
    listNumbers = []
    while n > 1:
        if n % i == 0:
            count = 0
            while n % i == 0:
                n = n // i
                count += 1
            listNumbers.append((i, count))
        i += 1
    if len(listNumbers) == 0:
        listNumbers.append((n, 1))
    return listNumbers

n = int(input("Nhập số nguyên dương n = "))
listNumbers = phanTichSoNguyen(n)

result = ""
for base, exponent in listNumbers:
    if exponent == 1:
        result += f"{base} * "
    else:
        result += f"{base}^{exponent} * "

result = result[:-3]  # Remove the extra ' * ' at the end
print("Kết quả:", n, "=", result)