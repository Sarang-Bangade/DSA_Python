class Deque:
    def __init__(self):
        self.items =[]

    def isEmpty(self):
        return len(self.items) == 0

    def insert_at_End(self,value):
        self.items.append(value)

    def delete_at_front(self,value):
        if(self.isEmpty()):
            print(f"Queue is empty")    
        else:
            return self.items.pop(0)
        
    def insert_at_front (self,value):
        self.items.insert(0,value)  

    def delete_at_end(self):
        if(self.isEmpty()):
            print(f"DQueue is empty")    
        else:
            return self.items.pop()

dq = Deque()
dq.insert_at_End(10)     
dq.delete_at_front(20)
dq.insert_at_End(30)
dq.insert_at_End(40)
dq.insert_at_front(50)

print(dq.delete_at_end())