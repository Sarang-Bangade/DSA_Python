class Node:
    def __init__(self, value = None):
        self.data = value
        self.next = None
        self.prev = None

class DoublyLL:
    def __init__(self):
        self.head = None


    def insert_at_end(self,value):
        temp = Node(value)
        if (self.head == None):
            self.head = temp
            return
        
        t = self.head
        while(t.next != None):
            t = t.next
        
        t.next = temp
        temp.prev = t


    def insert_at_beg(self ,value):
        temp = Node(value)
        if(self.head ==None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def insert_at_middle(self,value,x):
        t = self.head

        while(t.next != None):
            if(t.data == x):
                break
            else:
                t = t.next
        temp = Node(value)        
        temp.next = t.next
        t.next.prev = temp
        t.next = temp
        temp.prev = t

    def printDLL(self):
        t1 = self.head
        while (t1.next != None):
            print(t1.data , end=" <--> ")
            t1 = t1.next
        print(t1.data)

        
        
obj = DoublyLL()

obj.insert_at_end(10)        
obj.insert_at_end(20)        
obj.insert_at_end(30)
obj.insert_at_end(40)

obj.insert_at_beg(5)
obj.insert_at_middle(8,20)

obj.printDLL()