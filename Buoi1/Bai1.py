def openRussianDoll(doll):
    if doll == 1:
        print("All dolls are opened")
    else:
        openRussianDoll(doll-1)

doll = int(input('Nhập doll = '))

print(openRussianDoll(doll))