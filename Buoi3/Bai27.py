my_list = [2, 3, 5, 7]
target = 5

def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1

print(linear_search(my_list, target))