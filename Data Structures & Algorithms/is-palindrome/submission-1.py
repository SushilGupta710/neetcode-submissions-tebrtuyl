class Solution:
    def isPalindrome(self, s: str) -> bool:
        #standard solution without two pointer
        newStr=""
        for c in s:
            if(c.isalnum()):
                newStr+=c.lower()
        if(newStr == newStr[::-1]):
            return True
        else: return False

        