class Parenthesis:
    def __init__(self):
        self.stack = []
    def check(self,exp):
        for ele in exp:
            if ele =='{' or ele =='[' or ele =='(':
                self.stack.append(ele)
                continue
            if len(self.stack) ==0:
                print('####')
                return False
            if ele =='}':
                char = self.stack.pop()
                if char != '{':
                    return False
            if ele == ']':
                char = self.stack.pop()
                if char != '[':
                    return False
            if ele ==')':
                char = self.stack.pop()
                if char != '(':
                    return False
        if len(self.stack):
            return False
        else:
            return True

p = Parenthesis()

exp = input('Enter Expression')

if p.check(exp):
    print('This is balanced expression')
else:
    print('exp is not balanced')
