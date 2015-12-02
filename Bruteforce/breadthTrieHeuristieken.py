# Groupname: Aardbeizonder
# Names: Lucas Jollie, Bart Quaink, Anneke ter Schure
#
# File: breadthFirstBasic.py
# Goal: find the best solution with the least amount of steps
# -------------------------------------------------------------------------------

# imports
import time
import copy
from pythontrie import Trie

# initialise
queue = []
archive = Trie()
start_time = time.time()

class Node:
    """
    creates nodes for the graph needed for this type of search
    """
    def __init__(self, cargo=None, parent=None):
        self.cargo = cargo
        self.prev = parent

    def __str__(self):
        return str(self.cargo)

def GenerateAllChildren(parent):
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
                archive.insert(str(strConvparent))
                children.append(temp_parent)
        elif ((i == (length - 1) | i == (length - 2))):
            temp = temp_parentInv[i]
            temp_parentInv[i] = temp_parentInv[i-2]
            temp_parentInv[i-2] = temp
            strConvparentInv = copy.copy(temp_parentInv)
            if (archive.search(str(strConvparentInv)) == False):
                archive.insert(str(strConvparentInv))
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
            archive.insert(str(strConvparent))
            children.append(temp_parent)

# print "Children: ", children
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

    solution_found = False
    pare_node = Node(start)
    queue.append(pare_node)

    while (queue != [] and not solution_found):
        pare_node = queue.pop(0)
        c = GenerateAllChildren(pare_node.cargo)
        for i in range(len(c)):
            node = Node(c[i], pare_node)
#            if (archive.search(str(c[i])) == False):
#                archive.insert(str(c[i]))
            queue.append(node)
            if (c[i] == solution):
                print "Solution: ", c[i]
                solution_found = True
                inversions = 0
                while(node.prev != None):
                    print node
                    node = node.prev
                    inversions += 1
                print "Inversions: ", inversions

# starting point
# start = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
# solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
#start = [4,2,3,1]
#solution = [1,2,3,4]
#start = [4,2,3,1,6,8,7,5]
#solution = [1,2,3,4,5,6,7,8]
#start = [4,2,3,1,6,11,10,9,8,7,5]
#solution = [1,2,3,4,5,6,7,8,9,10,11]

runSimulation(start, solution)
print "---", (time.time() - start_time), "seconds ---"
