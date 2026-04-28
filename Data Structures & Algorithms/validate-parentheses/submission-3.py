class Solution:
    def isValid(self, s: str) -> bool:
        openCloseDict = {"}":"{",")":"(","]":"["}
        paranStack=[]
        for c in s:
            if paranStack and openCloseDict.get(c) == paranStack[-1]:
                paranStack.pop()
            else:
                paranStack.append(c)
        return True if not paranStack else False