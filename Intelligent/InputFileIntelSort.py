# import random module
import random
import ast

# open output and input files
steps = open("100genomesSwap.txt", 'w')
f = open("100randomgenomes.txt", "r")

for row in f.readlines():
    totalInversions = 0.0
    k = 0
    # assigne values of genomes
    preprow = row[:-1]
    preprow = preprow[1:]
    melan = preprow.split(', ')
    melan = [int(i) for i in melan]
    miran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
    print melan
    print type(melan)

    # definitions
    inversions = 0
    leng = len(melan) - 1
    runs = 0
    i = 0
    j = 0

    # writes start of trial
    steps.write("#")
    steps.write(str(k))
    steps.write(" Original: ")
    for i in range(len(melan)):
        steps.write(str(melan[i]))
        steps.write(",")
    steps.write(",")
    # steps.write("\n")

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
                    # steps.write(str(melan))
                    # steps.write("\n")

                # updates if is in place
                else:
                    runs += 1

            # visual representation of progress
            #if melan != miran:
            #    print runs
            #    print melan
            #print i, j

        # ensures loop starts after alreay ordened genes
        i = j

    # steps.write("Total number of inversions: ")
    steps.write(str(inversions))
    steps.write("\n")
    totalInversions += inversions
    k += 1

    print "Inversions: " + str(inversions)
    print "Solved Melanogaster: " + str(melan)

    steps.write("Mean inversions: ")
    steps.write(str(totalInversions / amount))
