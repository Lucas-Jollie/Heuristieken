# Groupname: Aardbeizonder
# Names: Lucas Jollie, Bart Quaink, Anneke ter Schure
#
# File: breadthFirstBasic.py
# Goal: find the best solution with the least amount of steps
#
# -------------------------------------------------------------------------------

# imports
import copy

# initialise
queue = []
archive = []
path = []
paths = open("path.txt", 'w')

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

    solution_found = False
    queue.append(start)

    while (queue != [] and not solution_found):
        parent = queue.pop(0)
        path.append(parent)
        paths.write(str(path))
        paths.write("\n")

        c = GenerateAllChildren(parent)
        for i in range(len(c)):
            print "C[i]: ", c[i]
            if (c[i] not in archive):
                archive.append(c[i])
                queue.append(c[i])
            elif (c[i] == solution):
                print "Solution: ", c[i]
                solution_found = True
                break

        print "queue: ", queue
        print "queue length: ", len(queue)

    print "path= ", path

# starting point
# Fruitfly.genome = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
# solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
start = [4,2,3,1]
solution = [1,2,3,4]

runSimulation(start, solution)
