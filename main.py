class Stack:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def push(self, item):
       self.items.append(item)

   def pop(self):
       return self.items.pop()

   def peek(self):
       return self.items[-1]


stack = Stack()

print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.is_empty())

print(stack.peek())



class Queue:
   def __init__(self):
       self.items = []

   def is_empty(self):
       return self.items == []

   def enqueue(self, item):
       self.items.insert(0, item)

   def dequeue(self):
       return self.items.pop()

   def size(self):
       return len(self.items)

queue = Queue()

print(queue.is_empty())

queue.enqueue("действие 1")
queue.enqueue("действие 2")
queue.enqueue("действие 3")
queue.enqueue("действие 4")

# ["действие 4", "действие 3", "действие 2", "действие 1"]

print(queue.is_empty())
print(queue.size())
print(queue.dequeue())
print(queue.size())



