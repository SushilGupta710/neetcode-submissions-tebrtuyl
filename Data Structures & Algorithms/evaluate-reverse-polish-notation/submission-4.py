class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        resultStack=[]
        for c in tokens:
            if c not in "+-*/":
                resultStack.append(int(c))
            else:
                a= resultStack.pop()
                b= resultStack.pop()
                
                if(c == "+"):
                    resultStack.append(a+b)
                elif(c == "-"):
                    resultStack.append(b-a)
                elif(c == "*"):
                    resultStack.append(a*b)
                elif(c == "/"):
                    resultStack.append(int(b/a))
        return resultStack[-1]