class Node:
    def __init__(self,info,link= None):
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
            while curr:
                print(curr.info)
                curr = curr.link
    def is_pallindrome(self):
        lst = []
        curr = self.head
        while curr:
            lst.append(curr.info)
            curr = curr.link
        curr = self.head
        flag = True
        count = 0
        while lst != []:
            ele = lst.pop()
            # print(ele)
            
            if ele == curr.info:
                count += 1
                curr = curr.link
            else:
                flag = False
                break
        if flag:
            print('list is pallindrome')
        else:
            print('list is not pallindrome')
ll = LinkedList()
ll.insert_at_beginning('k')
ll.insert_at_beginning('a')
ll.insert_at_beginning('y')
ll.insert_at_beginning('a')
ll.insert_at_beginning('k')
# ll.display()
ll.is_pallindrome()


