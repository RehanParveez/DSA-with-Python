# Q: Problem: Insert Node Between Increasing Order Break
## 1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def order(head, val):
#   new = Node(val)
#   curr = head
#   while curr.next:
#     curr = curr.next
#   curr.next = new
#   return head

# head = Node(5)
# head.next = Node(8)
# head.next.next = Node(10)
# head.next.next.next = Node(14)
# res = order(head, 8)

# while res:
#   print(res.data)
#   res = res.next
  
## 2
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def order(head, val):
#   new = Node(val)
#   if val < head.data:
#     new.next = head
#     return new
#   curr = head
#   while curr.next and curr.next.data < val:
#     curr = curr.next
#   new.next = curr.next
#   curr.next = new
#   return head

# head = Node(5)
# head.next = Node(8)
# head.next.next = Node(10)
# head.next.next.next = Node(15)
# res = order(head, 9)

# while res:
#   print(res.data)
#   res = res.next
  
  
## Q: Problem: Remove Nodes Smaller Than Next Node 
##1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def remove(head):
#   curr = head
#   while curr and curr.next:
#     if curr.data < head.data:
#       curr = curr.next
#     else:
#       break
#   return curr

# head = Node(6)
# head.next = Node(5)
# head.next.next = Node(10)
# head.next.next.next = Node(3)
# head.next.next.next.next = Node(8)
# res = remove(head)

# while res:
#   print(res.data)
#   res = res.next
  
## 2
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None
    
# def remove(head):
#   curr = head
#   prev = None

#   while curr and curr.next:
#     if curr.data < curr.next.data:
#       if prev:
#         prev.next = curr.next
#       else:
#         head = curr.next
#       curr = curr.next
#     else:
#       prev = curr
#       curr = curr.next
#   return head

# head = Node(5)
# head.next = Node(3)
# head.next.next = Node(10)
# head.next.next.next = Node(2)
# head.next.next.next.next = Node(8)

# res = remove(head)
# while res:
#   print(res.data)
#   res = res.next

## 3
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def remove(head):
#   prev = None
#   curr = head
#   while curr:
#     nxt = curr.next
#     curr.next = prev
#     prev = curr
#     curr = nxt
#   head = prev  

#   max = head.data
#   curr = head
#   while curr and curr.next:
#     if curr.next.data < max:
#       curr.next = curr.next.next
#     else:
#       curr = curr.next
#       max = curr.data

#   prev = None
#   curr = head
#   while curr:
#     nxt = curr.next
#     curr.next = prev
#     prev = curr
#     curr = nxt
#   return prev

# head = Node(5)
# head.next = Node(3)
# head.next.next = Node(10)
# head.next.next.next = Node(2)
# head.next.next.next.next = Node(8)

# res = remove(head)
# while res:
#     print(res.data)
#     res = res.next


## Q: Problem: Swap the first and last Nodes 
## 1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = None

# def swap(head):
#   first = head
#   curr = head
#   while curr.next:
#     curr = curr.next
#   last = curr
  
#   first.data, last.data = last.data, first.data
#   return head

# head = Node(6)
# head.next = Node(7)
# head.next.next = Node(8)
# head.next.next.next = Node(9)
# head.next.next.next.next = Node(10)
# res = swap(head)

# while res:
#   print(res.data)
#   res = res.next
  
## 2
# class Node:
#   def __init__(self, data):
#    self.data = data
#    self.next = None

# def swap(head):
#   prev = None
#   curr = head
  
#   while curr.next:
#     prev = curr
#     curr = curr.next
    
#   last = curr
#   prev.next = head
#   last.next = head.next
#   head.next = None
#   head = last
#   return head

# head = Node(6)
# head.next = Node(7)
# head.next.next = Node(8)
# head.next.next.next = Node(9)
# head.next.next.next.next = Node(10)
# res = swap(head)

# while res:
#   print(res.data)
#   res = res.next


## Q: Problem: Detect and remove cycle in a Linked List
## 1
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = next
    
# def cycle(head):
#   if head.next == head:
#     head.next == None
#   return head

# head = Node(11)
# head.next = Node(12)
# head.next.next = Node(13)
# head.next.next.next = Node(14)
# head.next.next.next.next = Node(15)

# res = cycle(head)
# while res:
#   print(res.data)
#   res = res.next

## 2
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = next
    
# def cycle(head):
#   if head.next == head:
#     head.next = None
#   return head

# head = Node(11)
# head.next = Node(12)
# head.next.next = Node(13)
# head.next.next.next = Node(14)
# head.next.next.next.next = Node(15)
# head.next.next.next.next.next = head.next.next

# res = cycle(head)
# while res:
#   print(res.data)
#   res = res.next

## 3
# class Node:
#   def __init__(self, data):
#     self.data = data
#     self.next = next

# def cycle(head):
#   slow = head
#   fast = head
  
#   # detect cycle
#   while fast and fast.next:
#     slow = slow.next
#     fast = fast.next.next
#     if slow == fast:
#       break
#   else:
#     return head
  
#   slow = head
#   while slow != fast:
#     slow = slow.next
#     fast = fast.next
    
#   ptr = fast
#   while ptr.next != fast:
#     ptr = ptr.next
#   ptr.next = None
  
#   return head

# head = Node(11)
# head.next = Node(12)
# head.next.next = Node(13)
# head.next.next.next = Node(14)
# head.next.next.next.next = Node(15)
# head.next.next.next.next.next = head.next.next

# res = cycle(head)
# while res:
#   print(res.data)
#   res = res.next


## Q: Problem: Merge the two Sorted Lists
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def merge(r, p):
  curr = r
  while curr.next:
    curr = curr.next
  curr.next = p
  return r

r = Node(1)
r.next = Node(5)
r.next.next = Node(9)

p = Node(3)
p.next = Node(7)
p.next.next = Node(11)

res = merge(r, p)
while res:
  print(res.data)
  res = res.next
