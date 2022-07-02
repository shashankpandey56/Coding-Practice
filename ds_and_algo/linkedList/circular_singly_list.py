class Node:
    def __init__(self,info,link= None):
        self.info = info
        self.link = link


class CircularSinglyList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,info):
        newNode = Node(info)
        if self.head == None:
            self.head = newNode
            self.head.next = self.head
        if self.head != None:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head 
            self.head = newNode
    def insert_at_end(self,info):
        newNode = Node(info)
        if self.head == None:
            self.head = newNode
            self.head.next = self.head
        if self.head != None:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = newNode
            newNode.next = self.head

    def delete_node(self,ele):
        if self.head == None:
            print('List is empty')
            return
        if self.head.info == ele:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
            return
        current = self.head 
        while current.next != self.head:
            if current.next.info == ele:
                temp = current.next
                current.next = temp.next
                temp = None
                return

            current = current.next
        print('Element is not found in the List')

    def display(self):
        if self.head == None:
            print('List is empty')
            return

        current = self.head 
        while current.next != self.head:
            print(current.info)
            current = current.next
        print(current.info)

csl = CircularSinglyList()
csl.insert_at_begining(10)
csl.insert_at_begining(8)
csl.insert_at_begining(4)
csl.display()
print('**************')
csl.insert_at_end(40)
csl.insert_at_end(60)
csl.display()
print('---------------')
csl.delete_node(60)
csl.delete_node(8)
csl.delete_node(4)
csl.display()
