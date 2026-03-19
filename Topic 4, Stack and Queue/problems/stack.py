## Q: Problem: The Check of Valid Parentheses:
## 1
# def valid(val):
#   c1 = 0
#   c2 = 0
#   for v in val:
#     if v == '(':
#       c1 = c1 + 1
#     if v == ')':
#       c2 = c2 + 1
#   if c1 == c2:
#     return True
#   else:
#     return False

# print(valid('('))  
# print(valid('()')) 
# print(valid(')(')) 

## 2
# def valid(val):
#   check = []
#   for v in val:
#     if v == '(':
#       check.append(v)
#     if v == ')':
#       if len(check) > 0:
#         check.pop()
#       else:
#         return False

#   if len(check) == 0:
#     return True
#   else:
#     return False

# print(valid('('))  
# print(valid('()')) 
# print(valid(')(')) 

## 3
# def valid(val):
#   check = []
  
#   for v in val:
#     if v == '(':
#       check.append(v)
#     elif v == '[':
#       check.append(v)
#     elif v == '{':
#       check.append(v)
    
#     elif v == ')':
#       if len(check) == 0:
#         return False
#       first = check[-1]
#       if first == '(':
#         check.pop()
#       else:
#         return False
    
#     elif v == ']':
#       if len(check) == 0:
#         return False
      
#       first = check[-1]
#       if first == '[':
#         check.pop()
#       else:
#         return False
    
#     elif v == '}':
#       if len(check) == 0:
#         return False
#       first = check[-1]
#       if first == '{':
#         check.pop()
#       else:
#         return False
    
#   if len(check) == 0:
#     return True
#   else:
#     return False 

# print(valid('(]'))  
# print(valid('()')) 
# print(valid(')(')) 
# print(valid('()[]{}')) 
# print(valid('([{}])')) 


## Q: Problem: Reverse a String
## 1
# def reverse(str):
#   return str[::-1]

# print(reverse('reverse')) 
# print(reverse('traverse'))

## 2
# def reverse(str):
#   check = []
  
#   for s in str:
#     check.append(s)
#   store = ''
#   for val in range(len(check)):
#     store = check[val]
#   return store

# print(reverse('reverse')) 
# print(reverse('traverse'))

## 3
def reverse(str):
  check = []
  
  for s in str:
    check.append(s)
  store = ''
  while len(check) > 0:
    s = check.pop()
    store = store + s
  return store

print(reverse('reverse'))
print(reverse('traverse'))
