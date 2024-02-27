def SumOfDigit(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + SumOfDigit(n//10)
    
n = int(input('Nhập n = '))

print(f'Tổng các chữ số của {n} là {SumOfDigit(n)}')