class Node():
    def __init__(self, data):    #constructor
        self.data = data
        self.next = None

class linklist():
    def __init__(self, head=None):
        self.head=head

    def insert(self, data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def print(self):
        current=self.head
        while current != None:
            print(current.data)
            current=current.next

    def ID(self):
        current = self.head
        current = current.next
        return (current.data)

    def NAME(self):
        current = self.head
        return (current.data)