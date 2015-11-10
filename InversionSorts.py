# Groupname: Aardbeizonder
# Members: Bart Quaink, Lucas Jollie, Anneke ter Schure
#
# File: InversionSort.py
# Goal: explore sorting functions that make use of inversions


# includes-----------------------------------------------------------------------
import random

# initialisations----------------------------------------------------------------
# original = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
# solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]

# functions ---------------------------------------------------------------------

# Old-fashioned inversion of size 2 going from left to right
def bubbleSort(a):
    count = 0
    changed = True
    while changed:
        changed = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                count += 1
                changed = True
    return count

# Inversion of size 3 or size 2 going from left to right
def b3Sort(a):
    count = 0
    changed = True
    while changed:
        changed = False
        for i in range(len(a) -2):
            if a[i] > a[i + 2]:
                temp = a[i]
                a[i] = a[i + 2]
                a[i + 2] = temp
                count += 1
            elif a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                count += 1
                changed = True
    return count

# Inversion of size 2 at random places
def randomBubbleSort(a):
    count = 0
    archive = []
    while True:
        i = random.randint(0, len(a) - 1)
        print "i is:", i
        j = i + 1
        if i < j:
            b = swap(a, i, j)
            if b not in archive:
                a = b
                count += 1
                archive.append(a)
        if is_sorted(a):
            return count

# function to invert a piece of list a between two indices: i and j
# range(chunk/2 + 1) is because you only need to swap half of the list!
def swap(a, i, j):
    if i > j:
        tmp = i
        i = j
        j = tmp
    chunk = j - i
    for k in range(chunk/2 + 1):
        temp = a[i]
        a[i] = a[j]
        a[j] = temp
        i += 1
        j -= 1
    return a

# function to check if list is sorted
def is_sorted(list):
    for i in range(0, len(list) - 1):
        if list[i] > list[i + 1]:
            return False
    return True

# checks ------------------------------------------------------------------------

a = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
print "Original:", a
print "Number of bubbleSort steps (size 2):", bubbleSort(a)
print "New:", a,"\n"

a = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
print "Original:", a
print "Number of bubbleSort steps (size 3):", b3Sort(a)
print "New:", a,"\n"

a = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
print "Original:", a
print "Number of random steps (size 2):", randomBubbleSort(a)
print "New:", a,"\n"
