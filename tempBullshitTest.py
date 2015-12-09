#import random

#beg = []

#end = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

#while len(beg) != 25:
#    r = random.randint(1,25)
#    if r not in beg:
#        beg.append(r)
#        
#print beg
#print end

#while end != beg:
#    
#    
#def A*(beg, end):
#    # open and to be closed nodes
#    closed = []
#    opend = []
#    for i in range(len(beg)):
#        opend.append(beg[i])


from heapq import *

heap = []
data = [(10,"ten"), (3,"three"), (5,"five"), (7,"seven"), (9, "nine"), (2,"two")]
for item in data:
    heappush(heap, item)
    print "heap ", heap
sorted = []
while heap:
    sorted.append(heappop(heap))
    print "sorted ",  sorted
    print "heap ", heap
print sorted
data.sort()
print data == sorted
