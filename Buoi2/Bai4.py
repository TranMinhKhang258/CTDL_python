def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))

a = [1, 3, 5, 7, 9]
b = [0, 2, 4, 6, 8]

printUnorderedPairs(a, b)