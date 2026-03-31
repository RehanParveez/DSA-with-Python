## Q: Problem: Implement Queue using List
## 1
# def enqueue(queue, n):
#   queue.append(n)
# def dequeue(queue, n):
#   return queue.pop(n) 

# queue = []
# enqueue(queue, 50)
# enqueue(queue, 100)
# enqueue(queue, 150)
# print(dequeue(queue, 0))
# print(dequeue(queue, 1))

## 2
# def enqueue(queue, n):
#   queue.append(n)
# def dequeue(queue):
#   return queue.pop(0)

# queue = []
# enqueue(queue, 50)
# enqueue(queue, 100)
# enqueue(queue, 150)
# print(dequeue(queue))
# print(dequeue(queue))

## 3
# from collections import deque
# def enqueue(queue, n):
#   queue.append(n)
# def dequeue(queue):
#   return queue.pop()

# queue = deque(str(0))
# enqueue(queue, 50)
# enqueue(queue, 100)
# enqueue(queue, 150)
# print(dequeue(queue))
# print(dequeue(queue))

## Q: Problem: Queue using Two Stacks
## 1
# class Queue:
#   def __init__(self):
#     self.check1 = []
#     self.check2 = []
    
#   def enqueue(self, n):
#     self.check1.append(n)
#   def dequeue(self):
#     if len(self.check1) != 0:
#       if len(self.check2) == 0:
#         self.check2.append(self.check1)
#     return self.check2

# queue = Queue()
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# print(queue.dequeue())
# print(queue.dequeue())

## 2
# class Queue:
#   def __init__(self):
#     self.check1 = []
#     self.check2 = []
  
#   def enqueue(self, n):
#     self.check1.append(n)
#   def dequeue(self):
#     if len(self.check2) == 0:
#       while len(self.check1) != 0:
#         self.check2.append(self.check1.pop())
#     return self.check2.pop()

# queue = Queue()
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# print(queue.dequeue())
# print(queue.dequeue())

## Q: Problem: First Non-Repeating Character in Stream
## 1
# def repeating(val):
#     queue = []
#     freq = {}
#     res = []

#     for v in val:
#       queue.append(v)
      
#       if v in freq:
#         freq[v] += 1
#       else:
#         freq[v] = 1
#       while len(queue) > 0:
#         # if freq(queue[0]) > 1:
#         #   queue.pop(0)
#         # if len(queue) == 0:
#         #   res.append(-1) 
        
# #     return res
# # print(repeating('aabbcd'))

#         if freq[queue[0]] > 1:
#           queue.pop(0)
#         else:
#           break
#         if len(queue) == 0:
#           res.append(-1) 
#         else:
#           res.append(queue[0])

#     return res
# print(repeating('aabbcd'))

## 2
from collections import deque
def repeating(val):
  queue = deque()
  freq = {}
  res = []

  for v in val:
    queue.append(v)
    if v in freq:
      freq[v] += 1
    else:
      freq[v] = 1

    while len(queue) > 0:
      if freq[queue[0]] > 1:
        queue = deque(list(queue)[1:])
      else:
        break
    if len(queue) == 0:
      res.append(-1)
    else:
      res.append(queue[0])

  return res
print(repeating('aabbcd')) 