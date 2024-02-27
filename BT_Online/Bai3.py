def reverse_integer(num):
    reversed_num = 0
    
    while num != 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num //= 10
    
    return reversed_num

original_number = 1234
reversed_number = reverse_integer(original_number)

print(f"Original Number: {original_number}")
print(f"Reversed Number: {reversed_number}")
