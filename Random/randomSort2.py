# Groupname: Aardbeizonder
# Members: Bart Quaink, Lucas Jollie, Anneke ter Schure
#
# File: randomSort2.py
# Goal: explore random sorting

# random inversion sort functions -----------------------------------------------

def randomBubbleSort(a):
    count = 0
    archive = []
    while is_sorted(a) == False:
        i = random.randint(0, len(a) - 1)
        j = random.randint(i + 1, len(a) - 1)
        if i < j:
            b = swap(a, i, j)
            if b not in archive:
                a = b
                count += 1
                archive.append(a)
        if is_sorted(a):
            return count

# helper functions --------------------------------------------------------------

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

# checks-------------------------------------------------------------------------

a = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
print "Original:", a
print "Number of random steps (size 2):", randomBubbleSort(a)
print "New:", a,"\n"
