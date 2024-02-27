def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
             for k in range(0,100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))

a = [1, 2, 3]
b = [4, 5, 6]

printUnorderedPairs(a, b)