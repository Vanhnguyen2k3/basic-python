# Chương trình 3.1
# khai bao bien a, b la so nguyen
a = 5
b = int(6)
print(a, b)

# Chương trình 3.2
a = int(input(" Nhap so nguyen a: "))
print(a)

# Chương trình 3.3
n1 = int(input(" Nhap so thu nhat: "))
n2 = int(input(" Nhap so thu hai: "))
print(" Tong cua 2 so: ", n1 + n2)

# Chương trình 3.4
# Khai bao bien a, b la so thuc
a = 5.2
b = float(6.7)
print(a, b)

# Chương trình 3.5
a = float(input(" Nhap so thuc a: "))
print(a)

# Chương trình 3.6
n1 = float(input(" So thu nhat: "))
n2 = float(input(" So thu hai: "))
print(" Tong cua 2 so: ", n1 + n2)

# Chương trình 3.7
try:
    a = int(input(" Nhap so nguyen: "))
except:
    a = 0
print(a)