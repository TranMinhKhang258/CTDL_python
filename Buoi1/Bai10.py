def DecToBin(n):
    if n == 0:
        return 0
    else:
        return (n % 2) + 10 * DecToBin(n // 2)
    
n = int(input('Nhập n = '))

print(f'Số nhị phân tương ứng của {n} là {DecToBin(n)}')