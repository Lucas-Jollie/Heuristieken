# Groupname: Aardbeizonder
# Names: Lucas Jollie, Bart Quaink, Anneke ter Schure
#
# A mix of beam and astar; uses a priority queue! and doesn't stop when solution found!
# only prints best solution!
# loops through the generations instead of just the priority queue
# -------------------------------------------------------------------------------

# imports
import time
import copy
import heapq
from pythontrie import Trie
from scoreDefs import generationScore
from heapq import *

# initialise
queue = []
archive = Trie()

#TODO adjust: ########################
beam = 600
maxQueue = 50
maxGenerations = 30
######################################

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

def generateAllChildren(parent):
    """
    Generates all children of parent
    Based on inversions of size 3
    """
    children = []
    length = len(parent)

    for i in range(length):
        for j in range(length):
            temp_parent = copy.copy(parent)
            if i != j:
                begin = copy.copy(i)
                end = copy.copy(j)
                while begin < end:
                    temp = temp_parent[end]
                    temp_parent[end] = temp_parent[begin]
                    temp_parent[begin] = temp
                    begin += 1
                    end -= 1
                string_parent = copy.copy(temp_parent)
                children.append(temp_parent)

    return children

def selectChildren(childrennodes, g):

    scores = []
    children = []
    genomes = []
    # calculate "fitness" scores
    for i in range(len(childrennodes)):
        if (childrennodes[i].cargo not in genomes):
            s = generationScore(childrennodes[i].cargo, g)
            scores.append(s)
            children.append(childrennodes[i])
            genomes.append(childrennodes[i].cargo)

    # check which 3 genomes have the best scores
    dictionary = heapq.nsmallest(beam, zip(scores, children))

    # put the best genomes in a list before returning
    best_children = []
    for j in range(len(dictionary)):
        best_children.append(dictionary[j][1])

    childrennodes = []
    scores = []
    return best_children

# algorithm
def runSimulation(start, solution):
    """
    Returns minumum number of time steps needed to get to solution
    """
    solutionNodes = []
    g = 0
    solution_found = False

    pare_node = Node(start)
    m = (0, pare_node)
    heappush(queue, m)

    while ((queue != []) and (g <= maxGenerations) and (solution_found == False)):
        nextGeneration = []
        print "--- Computing generation", g, "---"
        g += 1
        for b in range(beam):
            if (queue != []):
                pare_node = heappop(queue)
                children = generateAllChildren(pare_node[1].cargo)
                for i in range(len(children)):
                    # create nodes
                    node = Node(children[i], pare_node[1])
                    nextGeneration.append(node)

        c = selectChildren(nextGeneration, g)
        for i in range(len(c)):
            if (c[i].cargo == solution):
                solution_found = True
                solutionNodes.append(c[i])
                print "Solutions found:", len(solutionNodes)
                break
            else:
                score = generationScore(c[i].cargo, g)
                l = (score, c[i])
                if (len(queue) <= maxQueue):
                    heappush(queue, l)
                else:
                    heappushpop(queue, l)
        queue = []

    # only print shortest solutions
    lowest = 50
    inversions = 0
    for j in range(len(solutionNodes)):
        node = solutionNodes[j]
        while((node.prev != None) and (inversions < lowest)):
            print "Step", node
            node = node.prev
            inversions += 1
        if (inversions < lowest):
            lowest = inversions
            print "Inversions: ", inversions
            print "Start:", start
        j += 1

# starting points ##############################################################
# start = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
# solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# start = [2,1,4,3]
# solution = [1,2,3,4]

# start = [1,2,3,5,6,4]
# solution = [1,2,3,4,5,6]

# start = [1,2,7,3,5,6,4]
# solution = [1,2,3,4,5,6,7]

## size: 8 ##
# start = [4,2,3,1,6,8,7,5]
# solution = [1,2,3,4,5,6,7,8]

## size: 9 ##
# start = [1,2,3,4,6,8,9,7,5]
# solution = [1,2,3,4,5,6,7,8,9]

## size: 10 ##
start = [4,2,3,1,10,6,8,9,7,5]
solution = [1,2,3,4,5,6,7,8,9,10]

## size: 11 ##
# start = [4,2,3,1,6,11,10,9,8,7,5]
# solution = [1,2,3,4,5,6,7,8,9,10,11]

# start = [4,2,3,1,6,11,10,9,8,7,5]
# solution = [1,2,3,4,5,6,7,8,9,10,11]

stringsol = copy.copy(solution)

runSimulation(start, solution)
print "---", (time.time() - start_time), "seconds ---"
