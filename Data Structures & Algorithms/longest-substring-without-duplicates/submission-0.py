class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sett =set()
        length = len(s)
        l=0
        longest=0
        for r in range(length):
            while s[r] in sett:
                # remove previous element
                sett.remove(s[l])
                #increase l pointer
                l+=1
            #now get the width of string
            w=  (r-l) +1#because we need to conclude self ef 0-0=0+1 
            longest =max(longest,w)
            sett.add(s[r])
        return longest