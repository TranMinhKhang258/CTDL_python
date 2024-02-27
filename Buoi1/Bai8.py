def PowerOfNumber(a, b):
    if b == 0:
        return 1
    else:
        return a * PowerOfNumber(a, b-1)
    
a = int(input('Nhập a = '))
b = int(input('Nhập b = '))

print(f'Kết quả của {a} mũ {b} là {PowerOfNumber(a, b)}')