
class Node:
    def __init__(self,info,link = None):
        self.info = info
        self.link = link

class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self,info):
        new_node = Node(info)
        if self.head == None:
            self.head = new_node
        else:
            new_node.link = self.head 
            self.head = new_node
    def display(self):
        if self.head == None:
            print('List is empty')
            return
        else:
            curr = self.head
            while curr.link != None:
                print(curr.info)
                curr = curr.link
            print(curr.info)
    
    def rmove_from_last(self,pos):
        if self.head == None:
            print('List is empty')
            return
        else:
            current = self.head
            count =1
            while current.link != None:
                count += 1
                current = current.link
            if pos > count:
                print('Number of element is less than index')
            else:
                l = count - pos
                new_curr = self.head
                while l-1:
                    new_curr = new_curr.link
                    l = l-1
                temp = new_curr.link
                new_curr.link = temp.link
                temp = None
                return
    def optimized_code(self,pos):
        if self.head == None:
            print('List has no element')
            return 
        else:
            p = self.head
            q = self.head 
            while pos:
                q = q.link
                pos -= 1
            while q != None:
                q = q.link
                p = p.link
            print(p.info)
            
ll = LinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(4)
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
# ll.display()
# ll.show_value_from_last(3)
ll.optimized_code(3)
ll.rmove_from_last(3)
ll.display()
