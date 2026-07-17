# Day11_stack_queue_problems

##STACK
#Example:

class stack:
    def __init__(self):
        self.stack=[]
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        if len(self.stack)==0:
            print("no element")
        else:
            self.stack.pop()
    def peek(self):
        if len(self.stack)==0:
                print(self.stack[len(self.stack)-1])
    def display(self):
            print(self.stack)
    def isEmpty(self):
        print(len(self.stack))==0
    def size(self):
        print(len(self.stack))
s=stack()
s.push("a")
s.push("b")
s.pop()
s.display()
s.peek()
s.size()




##QUEUE:
#Example:
class queue:
    def __init__(self):
        self.queue=[]
    def Enque(self,element):
        self.queue.append(element)
    def Deque(self):
        self.queue.pop(0)
    def size(self):
        print(len(self.queue))
    def peek(self):
        print(self.queue[0])
    def isEmpty(self):
        print(len(self.queue)==0)
    def display(self):
        print(self.queue)
q=queue()
q.Enque('a')
q.Enque('b')
q.Deque()
q.size()
q.peek()
q.isEmpty()
q.display()
