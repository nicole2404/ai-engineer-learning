#Bài 01 - Xếp loại điểm
# score = float(input("Nhập điểm: "))
# if score >= 8:
#     print("Giỏi")
# elif score >= 6.5:
#     print("Khá")
# elif score >= 5:
#     print("Trung bình")
# else:
#     print("Chưa đạt")

#Bài 2 - kiểm tra điểm hợp lệ
# score = float(input("Nhập điểm: "))
# if score < 0 or score > 10:
#     print("Điểm không hợp lệ")
# elif score >= 8:
#     print("Giỏi")
# elif score >= 6.5:
#     print("Khá")
# elif score >= 5:
#     print("Trung bình")
# else:
#     print("Chưa đạt")

#Bài 3 - số chẵn/lẻ và âm/dương
# n = int(input("Nhập một số nguyên: "))
# if n == 0:
#     print("0")
# elif n < 0:
#     print("Âm")
# elif n > 0:
#     print("Dương")
# if n % 2 == 0 and n != 0:
#     print("Số chẵn")
# elif n % 2 != 0 and n != 0:
#     print("Số lẻ")

# Bài 4 — kiểm tra đăng nhập đơn giản.
# user_name = input("Nhập user name: ")
# password = input("Nhập Password: ")
# if user_name == "admin" and password == "123456":
#     print("Đăng nhập thành công!")
# else:
#     print("Sai tài khoản hoặc mật khẩu")

# Bài 5 — phân loại độ tuổi.
# age = int(input("Nhập tuổi: "))
# if age < 0:
#     print("Tuổi không hợp lệ")
# elif age >= 60:
#     print("Người cao tuổi")
# elif age >= 18:
#     print("Người lớn")
# elif age >= 13:
#     print("Thiếu niên")
# else:
#     print("Trẻ em")

# Bài 6 — kiểm tra năm nhuận
# year = int(input("Nhập năm: "))
# if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
#     print("Năm nhuận")
# else:
#     print("Năm không nhuận")

# Bài 7 — kiểm tra tam giác đơn giản.
# a = float(input("Nhập cạnh a: "))
# b = float(input("Nhập cạnh b: "))
# c = float(input("Nhập cạnh c: "))
# if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
#     print("Là tam giác")
# else:
#     print("Không phải tam giác")

# Bài 8 — tìm số lớn nhất trong 3 số.
# a = float(input("Nhập a: "))
# b = float(input("Nhập b: "))
# c = float(input("Nhập c: "))
# if a >= b and a >= c:
#     print(a)
# elif b >= a and b >= c:
#     print(b)
# else:
#     print(c)

# Bài 9 — kiểm tra điều kiện giảm giá.
# total = float(input("Nhập tổng tiền: "))
# is_member = int(input("Thành viên: "))
# if total >= 500000 or is_member == 1:
#     print("Được giảm giá")
# else: 
#     print("Không được giảm giá")

# Bài 10 — kiểm tra rút tiền ATM
# balance = float(input("Nhập số dư tài khoản: "))
# amount = float(input("Nhập số tiền muốn rút: "))
# if amount > 0 and amount <= balance and amount % 50000 == 0:
#     print("Rút tiền thành công")
# else:
#     print("Giao dịch không hợp lệ")

# Bài kiểm tra cuối D03
hours = int(input("Nhập số giờ gửi xe: "))
is_member = int(input("Thành viên: "))
if hours <= 0:
    print("Dữ liệu không hợp lệ")
elif hours > 5:
    if is_member == 1:
        print("Phí gửi xe: ",30000 - 5000)
    else:
        print("Phí gửi xe: ", 30000)
elif hours > 2:
    if is_member == 1:
        print("Phí gửi xe: ", 20000 - 5000)
    else:
        print("Phí gửi xe: ", 20000)
elif hours >= 1:
    if is_member == 1:
        print("Phí gửi xe: ", 10000 - 5000)
    else:
        print("Phí gửi xe: ", 10000)

