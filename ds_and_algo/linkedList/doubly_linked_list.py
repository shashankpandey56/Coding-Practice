class Node:
    def __init__(self,info,prev = None,next = None):
        self.info = info
        self.prev = prev
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self,ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
        else:

            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
    
    def insert_at_end(self,ele):
        newNode = Node(ele)
        if self.head == None:
            self.head = newNode
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = newNode
            newNode.prev = current

    def insert_at_position(self,info,pos,count=0):
        if pos <= 1:
            self.insert_at_begining(info)
        current = self.head
        while current.next != None:
            count += 1
            if pos-1 == count:
                newNode = Node(info)
                newNode.next = current.next
                current.next = newNode
                newNode.prev = current
                current.next.prev = newNode
            current = current.next
        else:
            self.insert_at_end(info)
    
    def delete_node(self,ele):
        if self.head == None:
            print('List is empty')
            return
        if self.head.next == None:
            if self.head.info == ele:
                temp = self.head
                self.head = None
                temp= None
                return
            else:
                print('element is not present in my list')
                return
        current = self.head
        while current.next != None:
            if current.info == ele:
                current.prev.next = current.next
                current.next.prev = current.prev
                current = None
                return
            current = current.next
        if temp.info == ele:
            temp.prev.next = None
            temp = None
            return
        print('Element is not found')


    def display(self):
        if self.head ==None:
            print('List is empty')
            return
        
        current = self.head
        while current != None:
            print(current.info)
            current = current.next
            




ll = LinkedList()

ll.insert_at_begining(10)
ll.insert_at_begining(5)
ll.display()
print('**************')
ll.insert_at_end(12)
ll.insert_at_end(16)
ll.display()
ll.insert_at_position(7,5)
print('#########')
ll.display()
ll.delete_node(16)
print('************')
ll.display()
