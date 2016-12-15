#!/usr/bin python3
import sys

def binary_search(sequence, lvalue, hvalue):    #n
        start = 0                               #1
        end = len(sequence)-1                   #1

        while start <= end:                     #n
            mid = (start+end)//2                #n

            if start > end:                     #1
                return  False                   #1
            elif hvalue <= sequence[mid]:       #n
                end = mid -1                    #n
            elif lvalue >= sequence[mid]:       #n
                 end = mid +1                   #n
            else:                               #n
                return True                     #1

            return Trus or False
#bigO=8n+5 = O(n)
        
sequence = [1, 3, 4, 6, 8, 9, 7]
lvalue = int(input("Low Value"))
hvalue = int(input("High Value"))
print(binary_search(sequence, lvalue, hvalue))
