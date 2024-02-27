import array

my_array = [1, 2, 3, 4, 5]

extra_value = [6, 7, 8, 9]
my_array.extend(extra_value)

print('Update after extend:')
print(my_array)