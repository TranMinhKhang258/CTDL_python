def factorial(n):
    if n < 0:
        return -1
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
n = int(input('Nhập n = '))

print(factorial(n))