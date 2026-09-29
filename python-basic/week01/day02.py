# ==========================================
# 🌟 THỰC HÀNH 1: Nhập xuất dữ liệu cơ bản
# ==========================================
# name = input("nhập tên của bạn: ")
# age = int(input("Nhập tuổi của bạn: "))
# print(name)
# print("Tuổi năm sau của bạn là: ", age + 1)
# print(type(name))
# print(type(age))


# ==========================================
# 🌟 THỰC HÀNH 2: Tổng số phút
# ==========================================
# minute = int(input("Nhập tổng số phút: "))
# print("Quy đổi sang giờ: ", minute//60, "giờ", minute%60, "phút")

# ==========================================
# 🌟 THỰC HÀNH 3: BMI
# ==========================================
# weight = int(input("Nhập cân nặng của bạn(kg): "))
# height = float(input("Nhập chiều cao của bạn(mét): "))
# BMI = weight / height ** 2
# print("BMI của bạn là: ",BMI)

# ==========================================
# 🌟 THỰC HÀNH 4: Tính tuổi
# ==========================================
# name = input("Nhập tên của bạn: ")
# date_of_birth = int(input("Nhập năm sinh của bạn: "))
# year_now = int(input("Nhập năm hiện tại: "))
# tinhtuoi = year_now - date_of_birth
# print("Xin chào", name)
# print("Năm nay",name, "khoảng:", tinhtuoi, "tuổi")

# #bài 18
# name = input("Nhập tên: ")
# age = int(input("Nhập tuổi: "))
# height = float(input("Nhập chiều cao: "))
# print("Xin chào", name)
# print("Năm sau bạn",age + 1, "tuổi")
# print("Chiều cao của bạn là",height,"mét")

# #bài 19
# minute = int(input("Nhập số phút: "))
# print("Kết quả: ", minute//60,"giờ",minute%60,"phút")

# #bài 20
# name1 = input("Tên của bạn là: ")
# weight = int(input("Cân nặng của bạn là: "))
# height2 = float(input("Chiều cao của bạn là: "))
# bmi = weight / height2**2
# print("Chỉ số BMI của ",name1, "là",bmi )

# #Bài 01: Giới thiệu bản thân
# name = input("Nhập tên của bạn: ")
# age = int(input("Nhập tuổi của bạn: "))
# print("Xin chào", name ,"!")
# print("Tuổi của ", name, "vào năm sau là:", age + 1,"tuổi")

#Bài 02: Máy tính mini
# a = float(input("Nhập giá trị a: "))
# b = float(input("Nhập giá trị b: "))
# tong = a + b
# hieu = a - b
# tich = a * b
# thuong = a / b
# print(tong)
# print(hieu)
# print(tich)
# print(thuong)

# #Bài 03: Đổi phút
# minute = int(input("Nhập số phút: "))
# print("Số giờ: ",minute//60)
# print("Số phút còn lại: ", minute%60)

#Bài 04: Tính số đơn giản
# weight = int(input("Nhập số cân nặng của bạn: "))
# height = float(input("Nhập chiều cao của bạn: "))
# bmi = weight / height**2
# print("Chỉ số BMI của bạn là: ", bmi)

#Bài cuối buổi
name = input("Nhập tên của bạn: ")
year_of_birth = int(input("Nhập năm sinh của bạn: "))
year_now = int(input("Nhập năm hiện tại: "))
print("Xin chào", name, "!")
print("Tuổi dự kiến trong năm hiện tại của", name, "là:", year_now - year_of_birth , "tuổi")
