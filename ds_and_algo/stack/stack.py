class Stack:
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []
    
    def push(self,ele):
        self.stack.append(ele)
    
    def pop(self):
        if not self.isEmpty():
            return self.stack.pop()
        else:
            return -1
    def peek(self):
        if not self.isEmpty():
            return self.stack[-1]
        else:
            return -1

s = Stack()

while True:
    print('push')
    print('pop')
    print('peek')
    print('exit')
    do = input('Input what exactly you want to do')
    if do == 'push':
        ele = int(input('Enter element you want to push'))
        s.push(ele)
    elif do == 'pop':
        ele = s.pop()
        if ele == -1:
            print('stack is empty')
        else:
            print('Deleted element from stack is = {}'.format(ele))
    elif do == 'peek':
        ele = s.peek()
        if ele == -1:
            print('stack is empty')
        else:
            print('Top element of stack is = {}'.format(ele))
    elif do == 'exit':
        break
    else:
        break

    