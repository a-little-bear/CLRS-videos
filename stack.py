class Stack():
    
    #init method of the class Stack
    def __init__(self):
        self.stack = []
    
    #add value to the back of the stack
    def push(self, value):
        self.stack.append(value)
     
    #remove the last value of the stack   
    def pop(self):
        return self.stack.pop(-1)
    
    #check is the stack empty or not
    def empty(self):
        return len(self.stack) == 0
    
    #get the size of the stack
    def size(self):
        return len(self.stack)
    
    #peek the stack's last value
    def top(self):
        return self.stack[-1]
    
    #print the stack list
    def __str__(self):
        return str(self.stack)