### sorting cool stuff ###
import random

def assign(minn, maxx):
    return random.randint(minn, maxx)
    

def swap(string, first, last):
    if last < first:
        while last < first:
            temp = last
            print first, last, temp
            last = first
            print first, last, temp
            first = temp
            print first, last, temp
    while last > first:
        temp = string[first]
        string[first] = string[last]
        string[last] = temp
        first += 1
        last -= 1
    return string

log = []


melan = [3, 1, 4, 2]
miran = [1, 2, 3, 4]

best = len(melan)

leng = len(melan) - 1

#i = assign(0, leng)
i = 0
#j = assign(0, leng)
j = i + 1

while j == i:
    j = assign(0, leng)
swap(melan, i, j)

print i, j, melan
