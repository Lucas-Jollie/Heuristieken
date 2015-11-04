# import random module
import random

steps = open("swaps.txt", 'w')

# define lists of melanogaster and miranda genomes
#melan = [2, 14, 3, 7, 20, 21, 23, 25, 9, 16, 18, 5, 1, 22, 24, 10, 19, 11, 17, 8, 4, 15, 13, 6, 12]
melan = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
miran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# define inversions and genome index
inversions = 0
leng = len(melan) - 1
critIndex = []
runs = 0
i = 0
j = 0

steps.write("Original: ")
steps.write(str(melan))
steps.write("\n")

while melan != miran:

    for i in range(0, leng + 1, 1):
        if (melan[i] == runs + 1):
            j = runs
            if (melan[i] != (i + 1)):
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
            else:
                runs += 1
        if melan != miran:
            print runs
            print melan
        print i, j
    i = j
        
print "Inversions: " + str(inversions)
print "Soled Melanogaster: " + str(melan)
#print melan
