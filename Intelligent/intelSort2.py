# import random module
import random

steps = open("swaps.txt", 'w')

# define lists of melanogaster and miranda genomes
melan = [21, 19, 14, 22, 18, 23, 25, 10, 6, 9, 1, 13, 2, 7, 5, 12, 8, 20, 24, 15, 17, 4, 11, 3, 16]
#melan = [25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
miran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

# definitions
inversions = 0
leng = len(melan) - 1
runs = 0
i = 0
j = 0

# opens text file with the original string
steps.write("Original: ")
steps.write(str(melan))
steps.write("\n")

# loop until equal
while melan != miran:

    # loops for length of genome
    for i in range(0, leng + 1, 1):
        
        # checks if value in string equals place of runth place in genome
        if (melan[i] == runs + 1):
            
            j = runs
            
            # checks if current gene not in right place of genome
            if (melan[i] != (i + 1)):
            
                # swapping algorithm
                while i > j:
                    temp = melan[j]
                    melan[j] = melan[i]
                    melan[i] = temp
                    i -= 1
                    j += 1
                
                # update amount of inversions and times run through string
                inversions += 1
                runs += 1
                # add each inversion to text file
                steps.write(str(melan))
                steps.write("\n")
            # updates if is in place
            else:
                runs += 1
        
        # visual representation of progress
        if melan != miran:
            print runs
            print melan
        print i, j
    
    # ensures loop starts after alreay ordened genes
    i = j
        
print "Inversions: " + str(inversions)
print "Soled Melanogaster: " + str(melan)
