# Groupname: Aardbeizonder
# Members: Bart Quaink, Lucas Jollie, Anneke ter Schure
#
# File: generatecoordinates.py
# TODO:
#   either: adjust to create locations for steps in the evolutionary path from
#           D. melanogaster to D. miranda?
#   or:     create locations so that 1 to 25 forms the shortest route
#           and create a start position like melanogaster in tsp.py

# melanogaster = [23,1,2,11,24,22,19,6,10,7,25,20,5,8,18,12,13,14,15,16,17,21,3,4,9]
# miranda = sorted(melanogaster)

import random

cities = 25

out_file = open("cities.txt", "w")
for i in range(cities):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    out_file.write(str(x))
    out_file.write(",")
    out_file.write(str(y))
    out_file.write("\n")
out_file.close()
