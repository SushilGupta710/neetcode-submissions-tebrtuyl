class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter={}
        #check the length are same
        if len(s) != len(t):
            return False
        
        #count all the elemet from s
        for c in s:
            counter[c] = counter.get(c,0)+1
        
        #decrease and check char are found in counter
        for c in t:
            if c not in counter or counter[c] == 0:
                return False
            counter[c]-=1
        
        #Return True because all the element are passed
        return True