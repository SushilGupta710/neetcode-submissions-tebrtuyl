class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        # Now in this solution it is O(s+t) TC because two loop required
        countS,countT={},{} #Here SC is O(s+t) because two variable memory
        #now iterate through the loop O(n) TC
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i],0) #we are using get because we should not get no key found
            countT[t[i]] = 1 + countT.get(t[i],0) #assign value in same loop because lenth are same we know
        
        #again new loop to compare both thestring O(n)TC
        for c in countS:
            if countS[c] != countT.get(c,0):
                return False
        
        return True

