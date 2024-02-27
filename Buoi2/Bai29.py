from array import array

char_array = array('b', [75, 104, 97, 110, 103, 115])

string_display = char_array.tobytes().decode('utf')

print('Update after translate to string:')
print(string_display)