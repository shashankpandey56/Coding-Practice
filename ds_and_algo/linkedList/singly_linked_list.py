class Node:

    def __init__(self,info,link = None):
        self.info = info
        self.link  = link


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self,info):
        new_node = Node(info)
        if self.head != None:
            new_node.link = self.head
            self.head = new_node
        else:
            self.head = new_node
    def insert_at_end(self,info):
        new_node = Node(info)
        if self.head != None:
            current = self.head
            while current.link != None:
                current = current.link
            current.link = new_node
        else:
            self.head = new_node

    def delete_node(self,ele):
        if self.head == None:
            print('List is empty')
            return
        if self.head.info == ele:
            temp = self.head
            self.head = temp.link
            temp = None
            return 
        else:
            current = self.head 
            while current.link != None:
                if current.link.info == ele:
                    temp = current.link
                    current.link = temp.link
                    temp = None
                    return
                current = current.link
            print('Element is not found in the list')

    def search(self,ele):
        if self.head == None:
            print('List is empty')
            return
        current = self.head 
        while current != None:
            if current.info == ele:
                print('Element is present in list')
                return

            current = current.link

    def display(self):
        current = self.head
        while current != None:
            print(current.info)
            current = current.link


            



ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.display()
print('#############')
ll.insert_at_end(7)
ll.insert_at_end(8)
ll.insert_at_end(10)
ll.delete_node(5)
ll.delete_node(8)
ll.search(7)
ll.display()
ll.delete_node(10)
print('@@@@@@@@@@@@@@@@@@')
ll.display()

