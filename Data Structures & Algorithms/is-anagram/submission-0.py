class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter={}
        #check the length are same
        if len(s) != len(t):
            return False
        
        #Count all the element in s string
        for char in s:
            if char in counter:
                counter[char] +=1
            else:
                counter[char] = 1
        
        #Check t string character are present in counter 
        #then Decrease it
        for char in t:
            if char in counter:
                counter[char] -=1
            else:
                return False
        
        #Check counter are set to 0
        for value in counter.values():
            if value !=0:
                return False
        
        return True