
class Node(object):
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

    def delNode(self, data):
        temp = self.head
        
        # if head is the key to be deleted
        if temp is not None:
            if temp.data == data:
                self.head = temp.nextNode
                temp = None
                self.size -= 1
                return
        
        # search for the key, keep track of prev node, as we need to change prev.next
        while temp is not None:
            if temp.data == data:
                self.size -= 1
                break
            prev = temp
            temp = temp.nextNode
        
        # if dats not present in linked list
        if temp == None:
            return 

        # unlink the node from linked list
        prev.nextNode = temp.nextNode
    
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
print ('Third item: ', myList.addNode(15))

print ('\nPrinting items in linked list before deletion..')
myList.printNode()

print ('\nDeleting items from linked lists..')
myList.delNode(10)

print ('\nPrinting items in linked list after deletion..')
myList.printNode()

print ('\nSize of linked list..')
print (myList.getSize())