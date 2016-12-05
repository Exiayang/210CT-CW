def reverse(start, end, sentence):    # n
    print(start, end)
    if start == end or end < start:     # n
        print(  "here" ) 
        return start                     # 1
    else:          #n
        print( "here2") 
        temp = sentence[start]
        sentence [start] = sentence [end]
        sentence [end] = temp
        reverse (start+1, end-1, sentence)
        print (sentence)           #4n

sentence = "This is awesome !".split()
reverse(0, len(sentence)-1, sentence)

#big0=7n+1 = O(n)
