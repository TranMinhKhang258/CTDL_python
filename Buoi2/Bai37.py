import numpy as np

two_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

def traverseArray(array):
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j])

traverseArray(two_array)