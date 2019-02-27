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
        curr = self.head
        while(curr.nextNode != None):
            print(curr.value)
            curr = curr.nextNode
        print(curr.value)
        
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
