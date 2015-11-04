# Groupname: Aardbeizonder
# Members: Bart Quaink, Lucas Jollie, Anneke ter Schure
#
# File: InversionSort.py
# Goal: explore sorting functions that make use of inversions


# includes-----------------------------------------------------------------------
import random

# functions ---------------------------------------------------------------------

# Old-fashioned inversion of size 2 going from left to right
def bubbleSort(a):
    count = 0
    for passnum in range(len(a) - 1, 0 , -1):
        for i in range(passnum):
            if a[i] > a[i + 1]:
                temp = a[i]
                a[i] = a[i + 1]
                a[i + 1] = temp
                count += 1
    return count

# Inversion of size 3 going from left to right
def b3Sort(a):
    count = 0
    while a != [1,2,3,4,5,6]:
        for passnum in range(0, len(a) - 2, 1):
            for i in range(passnum):
                if a[i] > a[i + 2]:
                    temp = a[i]
                    a[i] = a[i + 2]
                    a[i + 2] = temp
                    count += 1
    return count

# Inversion of size 4 going from left to right
def b4Sort(a):
    count = 0
    for passnum in range(0, len(a) - 4, 1):
        for i in range(passnum):
            if a[i] > a[i + 3]:
                temp = a[i]
                a[i] = a[i + 3]
                a[i + 3] = temp
                temp = a[i + 1]
                a[i + 1] = a[i + 2]
                a[i + 2] = temp
                count += 1
    return count

# Inversion of size 2 at random places
def randomBubbleSort(a):
    count = 0
    while (a != [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]):
        i = random.randint(1, 23)
        if a[i] > a[i + 1]:
            temp = a[i]
            a[i] = a[i + 1]
            a[i + 1] = temp
            count += 1
    return count


# checks ------------------------------------------------------------------------

a = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
print "Original:", a
print "Number of bubbleSort steps (size 2):", bubbleSort(a)
print "New:", a,"\n"

a = [1,6,3,4,2,5]
print "Original:", a
print "Number of bubbleSort steps (size 3):", b3Sort(a)
print "New:", a,"\n"

a = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
print "Original:", a
print "Number of bubbleSort steps (size 4):", b4Sort(a)
print "New:", a,"\n"

a = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
print "Original:", a
print "Number of random steps (size 2):", randomBubbleSort(a)
print "New:", a,"\n"
