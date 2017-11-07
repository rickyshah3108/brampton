ages = [1,5,6,3,7]
for otherindex in range(0, len(ages)):
    for index in range(0, len(ages)-1):
        if ages[index] > ages[index + 1]:
            temp = ages[index]
            ages[index] = ages[index + 1]
            ages[index + 1] = temp

for x in range (0, 5):
    print(ages[x])





