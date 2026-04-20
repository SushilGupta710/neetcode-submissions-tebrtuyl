class MinStack:

    def __init__(self):
        self.stack=[]
        self.minStack=[] #to store min value

    def push(self, val: int) -> None:
        self.stack.append(val) #add value in array
        #now we need to add min value into minStack
        minVal = min(val,self.minStack[-1] if self.minStack else val)
        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop() #remove last element from array
        self.minStack.pop() #also we need to remove the min value if stack value is removed

    def top(self) -> int:
        return self.stack[-1] #get the last or latest value from array
        

    def getMin(self) -> int:
        return self.minStack[-1] #to get the latest min value from minStack
        
