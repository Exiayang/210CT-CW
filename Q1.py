List = [9, 5, 1, 3, 8, 6, 7, 4]
from random import *

x = []
for i in range(0, len(List), 1):      #n    
    randNum = randint(0, len(List)-1) #n   # choose a number randomly form the List
    takenout = List.pop(randNum)      #n   # take out the random number
    x.append(takenout)                #n   # put the number to the new List
print(x)


#big0=4n = O(n)
