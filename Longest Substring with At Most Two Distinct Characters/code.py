def longest_sub(s):
    #sliding window
    left = 0
    right = 0

    #dictionary to maintain 2 characters at a time
    #also used to find the last minimum value of the character to increment the left pointer
    dict_char = {}
    max_len = 0
    while right <len(s):
        dict_char[s[right]]=right      #storing the character with the index value of the first occurence in the substring/window

        #deleting if the no of characters in the window exceeds 2
        #modifying the left pointer to point at the latest character so the window onyl has 2 characters at all times
        if len(dict_char)>2:
            min_idx = min(dict_char.values())
            left = min_idx + 1
            del(dict_char[s[min_idx]])

        # updating the max by comparing the newfound and the previous max
        max_len = max(max_len, right -left +1)
        right+=1
    
    return max_len
    
s = 'eceba'
print(longest_sub(s))
