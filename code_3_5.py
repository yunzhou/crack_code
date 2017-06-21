class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []
    def deque(self):
        if len(self.s2)==0 and len(self.s1)==0:
            return None
        else:
            if len(self.s2)==0:
                while(len(self.s1)!=0):
                    self.s2.append(self.s1.pop())
            return self.s2.pop()


    def peek(self):
        if len(self.s2)==0 and len(self.s1)==0:
            return None
        else:
            if len(self.s2)==0:
                while(len(self.s1)!=0):
                    self.s2.append(self.s1.pop())
            return self.s2[-1]

    def enqueue(self,v):
        self.s1.append(v)

if __name__ == '__main__':
    q=MyQueue()
    q.enqueue('x')
    q.enqueue('y')
    q.enqueue('z')
    q.enqueue('a')
    print(q.peek())
    print(q.peek())
    print(q.deque())
    print(q.deque())
    print(q.deque())
    q.enqueue('1')
    q.enqueue('2')
    q.enqueue('3')
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.deque())
    print(q.deque())
