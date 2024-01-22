# Python linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        ## case where struct is empty
        if not self.head:    ## what is happening  behind the scences?(if not none(True when struct is empty))
            self.head = Node(data)
        else:
        ## case where struct already contains elements
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)

# Usage
my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
# The linked list now contains two nodes, the first node's data is 1, and it points to the second node which contains data 2.