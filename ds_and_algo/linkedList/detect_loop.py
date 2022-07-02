class Node:
    def __init__(self,info,next = None):
        self.info = info
        self.next = next
    
class LinkedList:
    def __init__(self):
        self.head = None

    def detect_loop(self):
        dict1 ={}
        if self.head == None:
            print('List is empty')
            return
        else:
            curr = self.head
            found = False
            while True:
                if curr not in dict1.keys():
                    dict1[curr] =1
                    if curr == None:
                        break
                else:
                    found = True 
                    break
            if found:
                print('loop is found')
                return
            else:
                print('Loop is not found')
                return
    def detect_loop_optimized(self):
        if self.head == None:
            print('List is empty')
            return
        else:
            fast = self.head
            slow = self.head
            while (slow and fast) and fast.next:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    print('loop')
                    return

