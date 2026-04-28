class MinStack:

    def __init__(self):
        self.result =[]
        self.minVal=[]

    def push(self, val: int) -> None:
        self.result.append(val)
        minValue = min(val,self.minVal[-1] if self.minVal else val)
        self.minVal.append(minValue)

    def pop(self) -> None:
        self.result.pop()
        self.minVal.pop()

    def top(self) -> int:
        return self.result[-1]
        

    def getMin(self) -> int:
        return self.minVal[-1]
        
