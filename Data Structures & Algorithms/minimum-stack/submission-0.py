class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_val=math.inf

    def push(self, val: int) -> None:
        if self.stack:
            if val<self.min_val:
                self.stack.append(2*val-self.min_val)
                self.min_val=val
            else:
                self.stack.append(val)    
        else:
            self.min_val=val
            self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1]<self.min_val:
            value=self.min_val
            self.min_val=2*self.min_val-self.stack.pop()
        else:
            value=self.stack.pop()
        return value

    def top(self) -> int:
        if self.stack[-1]<self.min_val:
            value=self.min_val
        else:
            value=self.stack[-1]
        return value
        
    def getMin(self) -> int:
        return self.min_val
