import numpy as np

two_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def AccessElement(Array, RowIndex, ColIndex):
    if RowIndex >= len(Array) or ColIndex >= len(Array[0]):
        print('Incorrect Index')
    else:
        print(Array[RowIndex, ColIndex])

print('Element to access:')
AccessElement(two_array, 1, 2)