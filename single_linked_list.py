
class Node( object ):
    def __init__(self, data, nextNode = None):
        self.data = data
        self.nextNode = nextNode
        
    def __get__(self, instance, owner):
        return self.data, self.nextNode
    
    def __set__(self, instance, data, nextNode):
        self.data = data
        self.nextNode = nextNode

class LinkedList(object):
    def __init__(self, head = None, size = 0):
        self.head = head
        self.size = size
        
    def getSize(self):
        return self.size
    
    def addNode(self, data):
        newNode = Node(data, self.head)
        self.head = newNode
        self.size += 1
        return True
    
    def printNode(self):
        curr = self.head
        while curr:
            print (curr.data)
            print (curr.nextNode)
            curr = curr.nextNode
            

myList = LinkedList()

# remember first item always tail, last insert is head
print ('Inserting items to linked list..')
print ('First item: ', myList.addNode(5))
print ('Second item: ', myList.addNode(10))

print ('\nPrinting items in linked list..')
myList.printNode()

print ('\nSize of linked list..')
print (myList.getSize())