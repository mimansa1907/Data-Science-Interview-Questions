text1 = 'abcdefghiedcba'
text2 = 'dcba'

op = 2

# windowsize = len(text2)

def CountAnagrams(text1,text2):
    i = 0
    j = 0
    k = len(text2)

    text2_map = {}
    ## create hashmap for text2
    for s in text2:
        if s not in text2_map:
            text2_map[s] = 1
        else:
            text2_map[s] += 1
    
    count = len(text2_map)
    ana_count = 0
    
    while j < len(text1):
        
    
print(CountAnagrams(text1,text2))
        


       
