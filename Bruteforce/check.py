
import heapq
from Heuristieken import seriesScore

children = [[1,2,3,5,4], [2,5,4,1,3], [1,2,3,4,5], [5,4,3,2,1]]
scores = []

# calculate "fitness" scores
for i in range(len(children)):
    s = seriesScore(children[i])
    scores.append(s)

# check which 3 genomes have the best scores
dictionary = heapq.nlargest(3, zip(scores, children))

best_children = []
for j in range(len(dictionary)):
    best_children.append(dictionary[j][1])

print "Dict: ", dictionary
print "genomes: ", best_children
# print "genomes: ", dictionary[
