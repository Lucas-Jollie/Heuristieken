# import random module
import random
import ast
from random import shuffle
import matplotlib
import matplotlib.pyplot as plt
import time

# ask amount of genomes to generate
amount = input("How many genomes? ")

totalInversions = 0
totalRuns = 0

for k in range(amount):

    pX = []
    pY = []

    # assigne values of genomes
    melan = random.sample(xrange(1,26),25)
    miran = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]

    # definitions
    inversions = 0
    leng = len(melan) - 1
    runs = 0
    i = 0
    j = 0


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
                    pY.append(inversions)
                    runs += 1
                    pX.append(runs)

                # updates if is in place
                else:
                    runs += 1

        i = j

    totalRuns += (runs / amount)
    totalInversions += (inversions / amount)
    plt.plot(pX, pY)

    leastamount = pX[-1]

    if pX[-1] <= leastamount:
        leastamount = pX[-1]

    # print totalRuns
    # print totalInversions


    # print "Inversions: " + str(inversions)
    # print "Solved Melanogaster: " + str(melan)

print leastamount
plt.ylabel('# of inversions')
plt.xlabel('# of runs')
plt.show()
