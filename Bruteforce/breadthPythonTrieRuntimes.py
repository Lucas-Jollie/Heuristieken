# Groupname: Aardbeizonder
# Names: Lucas Jollie, Bart Quaink, Anneke ter Schure
#
# Goal: find the best solution with the least amount of steps
# Breadth first approach with bubble sort and a basic trie for archive
#
# NOTE: this version calculates average run times for solving random genomes
# of a given size!
# -------------------------------------------------------------------------------

# imports
import time
import random
import copy
from pythontrie import Trie

# initialise; NOTE: adjust number_of_runs and length of genome!
number_of_runs = 50
length = 10
queue = []

class Node:
    def __init__(self, cargo=None, parent=None):
        self.cargo = cargo
        self.prev = parent

    def __str__(self):
        return str(self.cargo)

def GenerateAllChildren(parent):
    """
    Generates all children of parent
    Based on inversions of size 2
    """
    children = []
    temp_parent = copy.copy(parent)

    for i in range(len(parent) - 1):
        if i != 0:
            temp_parent = copy.copy(parent)
        if i == len(temp_parent) - 1:
            return children
        temp = temp_parent[i]

        temp_parent[i] = temp_parent[i + 1]
        temp_parent[i + 1] = temp
        children.append(temp_parent)

    return children


# algorithm
def runSimulation(start, solution):
    """
    Returns minumum number of time steps needed to get to solution
    """

    # initialise stack where genomes can be pushed in
    # -------usage--------------
    # stack = [3, 4, 5]
    # stack.append(6) --> [3, 4, 5, 6]
    # stack.pop() --> [3, 4, 5]
    archive = Trie()
    solution_found = False
    pare_node = Node(start)
    queue.append(pare_node)

    while (queue != [] and not solution_found):
        pare_node = queue.pop(0)
        c = GenerateAllChildren(pare_node.cargo)
        for i in range(len(c)):
            node = Node(c[i], pare_node)
            if (archive.search(str(c[i])) == False):
                archive.insert(str(c[i]))
                queue.append(node)
            elif (c[i] == solution):
                # print "Solution: ", c[i]
                solution_found = True
                inversions = 0
                while(node.prev != None):
                    # print node
                    node = node.prev
                    inversions += 1
                # print "Inversions: ", inversions

start_time = time.time()
for i in range(number_of_runs + 1):
    start = random.sample(xrange(1, length + 1), length)
    solution = sorted(start)
    runSimulation(start, solution)

# starting point
# start = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
# solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
# start = [4,2,3,1]
# solution = [1,2,3,4]
start = [4,2,3,1,6,8,7,5]
solution = [1,2,3,4,5,6,7,8]
#start = [4,2,3,1,6,11,10,9,8,7,5]
#solution = [1,2,3,4,5,6,7,8,9,10,11]

print "---", (time.time() - start_time)/number_of_runs, "seconds ---"
