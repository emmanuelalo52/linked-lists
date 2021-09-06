from Node import*
class LinkedList(object):
    def __init__(self):
        self.head=None
        self.counter = 0
#linear time complexity
    def traverselist(self):
        actualNode = self.head
        while actualNode is not None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode
    def reverselist(self):
        actualNode = self.head
        if actualNode is not None:
            actualNode = actualNode.nextNode
            return
        while actualNode is None:
            print("%d" % actualNode.data)
            actualNode = actualNode.nextNode
    # insering data at the start;O(1) using constant time complexity
    def insertstart(self,data):
        self.counter += 1
        newNode=Node(data)
        if not self.head:
            self.head = newNode
        else:
            newNode.nextNode= self.head
            self.head=newNode
    #using linear time complexity; that is O(1) instead of O(N)
    def size(self):
        return self.counter
    #inserting at the end using linear time complexity O(N)
    def insertEnd(self,data):
        if self.head is None:
            self.insertstart(data)
            return
        self.counter +=1
        newNode = Node(data)
        actualNode=self.head  
        while actualNode.nextNode is not None:
            actualNode=actualNode.nextNode
        actualNode.nextNode=newNode
    def remove(self,data):
        self.counter += 1 
        if self.head:
            if data == self.head.data:
                self.head=self.head.nextnode
            else:
                self.head.remove(data,self.head)