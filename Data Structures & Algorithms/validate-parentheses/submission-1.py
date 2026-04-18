class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]#empty array
        openClosePar={
            ")":"(",
            "}":"{",
            "]":"["
        }

        for c in s:
            #check firsrt c is present in ParDict
            if c in openClosePar:
                #in this also check if c value there in stack then remove it
                #before that check stack is not empty
                #and also check the previous value are matchig or not
                if stack and stack[-1] == openClosePar[c]:
                    stack.pop()
                else:
                    return False #here we know that stack previous value is not equal or open so this is invalid
            else:#add it
                stack.append(c)
        #after all the valid opetation complete we need to again check stack is not empty
        return True if not stack else False