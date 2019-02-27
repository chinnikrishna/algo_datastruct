class Node:
    def __init__(self, data, nextNode=None):
        self.value = data
        self.nextNode = nextNode

class SingleLL:
    def __init__(self):
        self.head = None
        
    def prepend(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
        else:
            temp = self.head
            self.head = n
            n.nextNode = temp
    
    def append(self, data):
        n = Node(data)
        if self.head == None:
            self.head = n
        else:
            curr = self.head
            while(curr.nextNode != None):
                curr = curr.nextNode
            curr.nextNode = n
    
    def printList(self):
        if self.head != None:
            curr = self.head
            while(curr.nextNode != None):
                print(curr.value)
                curr = curr.nextNode
            print(curr.value)
        else:
            print("Empty List")
        
    def delFirstNode(self):
        if self.head == None:
            print("Empty List")
        else:
            curr = self.head
            self.head = curr.nextNode
            del curr
    
    def delLastNode(self):
        if self.head == None:
            print("Empty List")
        else:
            curr = self.head
            while(curr.nextNode != None):
                temp = curr
                curr = curr.nextNode
            temp.nextNode = None
            del curr
            
    def revList(self):
        if self.head != None:
            nxt = None
            prv = None
            cur = self.head
            while (cur != None):
                nxt = cur.nextNode
                cur.nextNode = prv
                prv = cur               
                cur = nxt
            self.head = prv
        else:
            print("Empty List")


class DoubleNode(Node):
    def __init__(self, data):
        super().__init__(data)
        self.prevNode = None
    

class DoubleLL:
    def __init__(self):
        self.head = None
        self.tail = None
        
    def prepend(self, data):
        n = DoubleNode(data)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            curr = self.head
            self.head = n
            n.nextNode = curr
            curr.prevNode = n
    
    def append(self, data):
        n = DoubleNode(data)
        if self.head == None:
            self.head = n
            self.tail = n
        else:
            curr = self.tail
            self.tail = n
            n.prevNode = curr
            curr.nextNode = n
    
    def printList(self):
        if self.head != None:
                curr = self.head
                while(curr.nextNode != None):
                    print(curr.value)
                    curr = curr.nextNode
                print(curr.value)
        else:
            print("Empty List")

    def delFirstNode(self):
        if self.head != None:
            curr = self.head
            self.head = curr.nextNode
            del curr
        else:
            print("Empty List")
    
    def delLastNode(self):
        if self.head != None:
            curr = self.tail
            self.tail = curr.prevNode
            self.tail.nextNode = None
            del curr
        else:
            print("Empty List")