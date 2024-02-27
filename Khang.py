def average(*num):
    tmp = 0
    count = 0
    # duyet cac tham so
    for i in num:
        tmp += i
        count += 1
    return tmp / count


