def lengthOfLongestSubstring(s):
    #import pdb
    #pdb.set_trace()
    max_len  = 0
    start    = 0
    usedChar = {}
        
    for i in range(len(s)):
        if s[i] in usedChar and start <= usedChar[s[i]]:
            start = usedChar[s[i]] + 1
        else:
            max_len = max(max_len,i-start+1)
            
        usedChar[s[i]] = i
            
    return max_len  




print(lengthOfLongestSubstring('abcabcd'))
