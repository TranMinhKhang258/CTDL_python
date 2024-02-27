import numpy as np

two_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

new_two_array = np.insert(two_array, 1 , [10, 11, 12], axis=0)

print('Update after new_two_array;')
print(new_two_array)