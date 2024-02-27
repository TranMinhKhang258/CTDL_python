def reverse_array_in_place(arr):
    start = 0
    end = len(arr) - 1

    while start < end:
        arr[start], arr[end] = arr[end], arr[start]

        start += 1
        end -= 1

input_array = [1, 2, 3, 4, 5]
reverse_array_in_place(input_array)
print(input_array)