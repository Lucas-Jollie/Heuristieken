# def fucntion
#   set random start genomes
#   keep track of first swap
#

import random
from collections import deque

genomes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
random_list = random.sample(xrange(1,26),25)

print random_list
random_list.sort()
print random_list

from collections import deque

def bfs(g, start):
    queue, enqueued = deque([(None, start)]), set([start])
    while queue:
        parent, n = queue.popleft()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        queue.extend([(n, child) for child in new])

def dfs(g, start):
    stack, enqueued = [(None, start)], set([start])
    while stack:
        parent, n = stack.pop()
        yield parent, n
        new = set(g[n]) - enqueued
        enqueued |= new
        stack.extend([(n, child) for child in new])

def shortest_path(g, start, end):
    parents = {}
    for parent, child in bfs(g, start):
        parents[child] = parent
        if child == end:
            revpath = [end]
            while True:
                parent = parents[child]
                revpath.append(parent)
                if parent == start:
                    break
                child = parent
            return list(reversed(revpath))
    return None # or raise appropriate exception

if __name__ == '__main__':
    # a sample graph
    graph = {'1': ['2', '3','4'],
             '2': ['1','2', '5'],
             '3': ['4'],
             '4': ['3'],
             '5': ['6', '4'],
             '6': ['3']}

    print(shortest_path(graph, '1', '4'))
