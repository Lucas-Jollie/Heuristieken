# Groupname: Aardbeizonder
# Names: Lucas Jollie, Bart Quaink, Anneke ter Schure
#
# File: amix.py
# A mix of beam and astar; uses a priority queue!
#
# time and memory checks: http://www.huyng.com/posts/python-performance-analysis/
# paste:  @profile above the code you want to check
# for time check: $ kernprof -l -v 'amix.py' > timeramix.txt
#
# -------------------------------------------------------------------------------

# imports
import time
import copy
import heapq
from pythontrie import Trie
from Heuristieken import seriesScore
from heapq import *

# initialise
queue = []
archive = Trie()

start_time = time.time()

class Node:
    """
    creates nodes for the graph needed for this type of search
    """
    def __init__(self, cargo=None, parent=None, score=None):
        self.cargo = cargo
        self.prev = parent
        # self.score = score

    def __str__(self):
        return str(self.cargo)

# @profile
def generateAllChildren(parent):
    """
    Generates all children of parent
    Based on inversions of size 3
    """
    children = []
    temp_parent = copy.copy(parent)
    temp_parentInv = copy.copy(parent)
    length = len(parent)



    for i in range(length - 2):
        if i != 0:
            temp_parent = copy.copy(parent)
            temp_parentInv = copy.copy(parent)
        if ((i < length - 2)):
            temp = temp_parent[i]
            temp_parent[i] = temp_parent[i + 2]
            temp_parent[i + 2] = temp
            strConvparent = copy.copy(temp_parent)
            if (archive.search(str(strConvparent)) == False):
                children.append(temp_parent)
        elif ((i == (length - 1) | i == (length - 2))):
            temp = temp_parentInv[i]
            temp_parentInv[i] = temp_parentInv[i-2]
            temp_parentInv[i-2] = temp
            strConvparentInv = copy.copy(temp_parentInv)
            if (archive.search(str(strConvparentInv)) == False):
                children.append(temp_parentInv)

    for i in range(len(parent) - 1):
        if i != 0:
            temp_parent = copy.copy(parent)
        if i == len(temp_parent) - 1:
            return children

        temp = temp_parent[i]
        temp_parent[i] = temp_parent[i + 1]
        temp_parent[i + 1] = temp
        strConvparent = copy.copy(temp_parent)

        if (archive.search(str(strConvparent)) == False):
            children.append(temp_parent)

    for j in range(len(children)):
        archive.insert(str(children[j]))

    return children

# @profile
def selectChildren(children):

    scores = []
    # calculate "fitness" scores
    for i in range(len(children)):
        s = 1 - (seriesScore(children[i])/len(start))
        scores.append(s)

    # check which 3 genomes have the best scores
    dictionary = heapq.nsmallest(3, zip(scores, children))

    # put the best genomes in a list before returning
    best_children = []
    for j in range(len(dictionary)):
        best_children.append(dictionary[j][1])

    children = []
    scores = []
    return best_children

# algorithm
# @profile
def runSimulation(start, solution):
    """
    Returns minumum number of time steps needed to get to solution
    """

    solution_found = False
    pare_node = Node(start)
    m = (0, pare_node)
    heappush(queue, m)

    while (queue != [] and not solution_found):
        pare_node = heappop(queue)
        children = generateAllChildren(pare_node[1].cargo)

        c = selectChildren(children)
        for i in range(len(c)):
            score = seriesScore(c[i])
            node = Node(c[i], pare_node[1])
            l = (score, node)
            heappush(queue, l)
            if (c[i] == solution):
                print "Solution: ", c[i]
                solution_found = True
                inversions = 0
                while(node.prev != None):
                    print node
                    node = node.prev
                    inversions += 1
                print "Inversions: ", inversions

# starting points ##############################################################
#start = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
start = [23, 1, 2, 11, 24, 22, 19, 6, 10, 7, 25, 20, 5, 8, 18, 12, 13, 14, 15, 16, 17, 21, 3, 4, 9]
solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# start = [4,1,2,3]
# solution = [1,2,3,4]

## size: 8 ##
start = [4,2,3,1,6,8,7,5]
solution = [1,2,3,4,5,6,7,8]

## size: 9 ##
# start = [1,2,3,4,6,8,9,7,5]
# solution = [1,2,3,4,5,6,7,8,9]

## size: 10 ##
# start = [4,2,3,1,10,6,8,9,7,5]
# solution = [1,2,3,4,5,6,7,8,9,10]

## size: 11 ##
<<<<<<< HEAD
# start = [4,2,3,1,6,11,10,9,8,7,5]
# solution = [1,2,3,4,5,6,7,8,9,10,11]
=======
#start = [4,2,3,1,6,11,10,9,8,7,5]
#solution = [1,2,3,4,5,6,7,8,9,10,11]
>>>>>>> 73ffac82d8a5a076faecb8c14b4bfb0b5e94d424

runSimulation(start, solution)
print "---", (time.time() - start_time), "seconds ---"
