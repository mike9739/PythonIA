class Stack:
    def __init__(self):
        self.stack = []

    def push(self,data):
        if data not in self.stack:
            self.stack.append(data)
            return True
        else:
            return False
   
    def peek(self):
        return self.stack[0]
    
    def remove(self):
        #comprueba si la pila esta vacia
        if len(self.stack)<=0:
            return ('La pila esta vacia')
        else:
            return self.stack.pop()







