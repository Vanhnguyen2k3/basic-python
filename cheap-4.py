# Chương trình 4.1
a = 100
b = 10
if b == a:
    print("b bang a")

# Chương trình 4.2
a = 100
b = 10
if b == a:
    print("b bang a")
else:
    print("a khac b")

# Chương trình 4.3
a = 200
b = 10
if a < b:
    print("a be hon b")
elif a == b:
    print("a bang b")
else:
    print("a lon hon b")

# Chương trình 4.4
a = 2
b = 3
if a > 1:
    if b > 4:
        a = a + 1
        b = b + 1
    else:
        a = a + 2
        b = b + 2
    print(a, b, sep=" - ")

# Chương trình 4.5
num = float(input("Nhap mot so "))
if num % 2 == 0:
    print("So chan")
else:
    print("So le")

# Chương trình 4.6
num = float(input("Nhap mot so "))
if num >= 0:
    if num == 0:
        print("So khong")
    else:
        print("So duong")
else:
    print("So am")

# Chương trình 4.7
print("Phuong trinh bac nhat: ax + b = 0")
a = int(input("a = "))
b = int(input("b = "))
if (a == 0):
    print("Phuong trinh vo nghiem")
else:
    x = -b/a
print("nghiem cua phuong trinh: x = ", x)

# Chương trình 4.8
from math import sqrt
print("Phuong trinh bac hai: ax^2 + bx + c = 0")
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phuong trinh vo so nghiem!")
        else:
            print("Phuong trinh vo nghiem!")
    else:
        if c == 0:
            print("Phuong trinh co 1 nghiem x = 0")
        else:
            x = -c/b
            print("Phuong trinh co 1 nghiem x = ", x)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phuong trinh vo nghiem!")
    elif delta == 0:
        x = -b/(2 * a)
        print("Phuong trinh co 1 nghiem x = ", x)
    else:
        print("Phuong trinh có 2 nghiem phan biet!")
        x1 = float((-b - sqrt(delta)) / (2 * a))
        x2 = float((-b + sqrt(delta)) / (2 * a))
        print("x1 = ", x1)
        print("x2 = ", x2)