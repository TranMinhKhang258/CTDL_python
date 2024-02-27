from array import array

int_array = array('i', [1, 2, 3, 4, 5])

add_value = [6, 8, 10]
int_array.fromlist(add_value)

print('Update after add this item from the lisst:')
print(int_array)
