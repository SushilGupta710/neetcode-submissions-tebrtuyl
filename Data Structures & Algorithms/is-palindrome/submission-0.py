class Solution:
    def isPalindrome(self, s: str) -> bool:
        #standard solution 
        newStr=""
        for c in s:
            if(c.isalnum()):
                newStr+=c.lower()
        reverseString=newStr[::-1]
        if(reverseString == newStr):
            return True
        else: return False

        