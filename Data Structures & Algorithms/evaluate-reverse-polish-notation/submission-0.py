class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stacks=[]

        for c in tokens:
            #we know that we need to perform 4 operation
            if(c == "+"):
                a,b=stacks.pop(),stacks.pop()
                stacks.append(a+b)
            elif(c == "-"):
                a,b=stacks.pop(),stacks.pop()
                stacks.append(b-a)
            elif(c == "*"):
                a,b=stacks.pop(),stacks.pop()
                stacks.append(a*b)
            elif(c == "/"):
                a,b=stacks.pop(),stacks.pop()
                stacks.append(int(b/a))
            else:#we know here it is a digit
                stacks.append(int(c))
        return stacks[-1]