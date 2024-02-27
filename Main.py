def UCLN(a, b):
    if b == 0:
        return a
    else:
        return UCLN(b, a % b)

a = int(input('Nhập a = '))
b = int(input('Nhập b = '))

print(f'Ước chung lớn nhất của {a} và {b} là {UCLN(a, b)}')