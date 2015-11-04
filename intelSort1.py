# import random module
import random

steps = open("swaps.txt", 'w')

# define lists of melanogaster and miranda genomes
melan = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
miran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# define inversions and genome index
inversions = 0
leng = len(melan) - 1
critIndex = []
runs = 1
i = 0
j = 0

while melan != miran:

    for i in range(0, leng + 1, 1):
        if melan[i] == runs:
            j = runs - 1
            while i > j:
                temp = melan[j]
                melan[j] = melan[i]
                melan[i] = temp
                i -= 1
                j += 1
            inversions += 1
            runs += 1
            steps.write(str(melan))
            steps.write("\n")
        if melan != miran:
            print runs
            print melan
    i = j
        
print "Inversions: " + str(inversions)
print "Soled Melanogaster: " + str(melan)
#print melan
