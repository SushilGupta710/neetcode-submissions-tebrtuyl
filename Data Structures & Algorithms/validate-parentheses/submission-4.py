class Solution:
    def isValid(self, s: str) -> bool:
        openCloseDict = {"}":"{",")":"(","]":"["}
        paranStack=[]
        for c in s:
            if c in openCloseDict:
                if paranStack and paranStack[-1] == openCloseDict[c]:
                    paranStack.pop()
                else:
                    return False
            else:
                paranStack.append(c)
        return True if not paranStack else False