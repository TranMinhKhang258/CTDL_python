numdays = int(input("How many day's temperature? "))
total = 0
temp = []
for i in range(numdays):
    nextday = int(input("Day " + str(i) +"'s high temp: "))
    temp.append(nextday)
    total += temp[i]

avg = round(total/numdays,2)
print("\nAverage = " + str(avg))

above = 0
for i in temp:
    if i > avg:
        above += 1

print(str(above) + " day(s) above average")