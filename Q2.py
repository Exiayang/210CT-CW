def Trailing_Zeroes(x):                  #n       
    fives = 0                                      
    for number in range(2, x+1):         #n               
        while number > 0:                #n         
            if number % 5 == 0:          #n        
                fives += 1               #n      
                number = number/5        #n              
            else:                        #n             
                break                    #n            
    return fives                         #n          

print(Trailing_Zeroes(125))              #1       

#big0=9n+1 = O(n)
