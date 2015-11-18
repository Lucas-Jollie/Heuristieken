# tips: http://pythonprogramming.net/graphing-monte-carlo/?completed=/more-monte-carlo-comparison/


# import random
#
# def genome():
#     gen = random.randint(1,25)
#     if gen != 1:
#         return False
#     else:
#         return True
#
# x = 0
# while x < 100:
#     result = genome()
#     if result:
#         print result
#         x += 1

import ast
import random
from random import shuffle
import matplotlib
import matplotlib.pyplot as plt
import time

# ask amount of genomes to generate
amount = input("How many genomes? ")

genomes = [1,2,3,4,5]
start_time = time.time()

random_list = random.sample(xrange(1,6),5)

def plotting(random_list, genomes, start_time):
    pX = []
    pY = []
    shuffles = 0

    while random_list != genomes:
        shuffled = shuffle(random_list)
        shuffles += 1
        current_time = time.time() - start_time
        pX.append(current_time)
        pY.append(shuffles)
        print random_list
    if random_list == genomes:
        elapsed_time = time.time() - start_time
        pX.append(elapsed_time)
        pY.append(shuffles)
        print elapsed_time, ' seconds'

    plt.plot(pX, pY)
    print 'number of shuffles: ', shuffles

plotting(random_list, genomes, start_time)

plt.ylabel('# of iterations')
plt.xlabel('# of runs')
plt.show()
