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


# checks ------------------------------------------------------------------------

a = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
print "Original:", a
print "Number of bubbleSort steps (size 2):", bubbleSort(a)
print "New:", a,"\n"

a = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
print "Original:", a
print "Number of bubbleSort steps (size 3):", b3Sort(a)
print "New:", a,"\n"
