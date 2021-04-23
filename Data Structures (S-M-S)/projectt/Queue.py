class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Queue:
    def __init__(self):
        self.front=None
        self.head=None

    def Insert(self,element):
        new_node = Node(element)
        if self.front == None and self.head == None:
            self.front=new_node
            self.head=new_node
        else:
            self.head.next=new_node
            self.head=new_node

    def Delete(self):
        cur=self.front
        if cur != None:
            ret=self.front.data
            self.front=cur.next
        else:
            print('Empty')
        return ret

    def printq(self):
        cur=self.front
        while cur != None:
            print(cur.data)
            cur=cur.next
    def NAME(self):
        cur=self.front
        cur = cur.next
        return cur.data

    def ID(self):
        cur=self.front
        return cur.data

    def Search(self,element):
        cur = self.front
        while cur != None:
            if cur.data == element:
                return cur.data
            cur = cur.next

