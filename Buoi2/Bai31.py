from array import array

my_array = array('b', [87, 101, 108, 99, 111, 109, 101])

string_append = ' Khangs'

new_char = array('b', map(ord, string_append))

my_array.extend(new_char)

print('Update after string_append:')
print(my_array)