## Q: Problem: The infinite undo buffer (Tutorial Practice)

## Goal: Assign a unique ID to every unique string.
## 1
# states = {}
# counter = 0

# def get_id(text):
#   global counter
#   key = len(text) 
  
#   if key in states:
#     return states[key]
#   else:
#     counter = counter + 1
#     states[key] = counter
#     return counter

# print(get_id('cat'), get_id('dog'))

## 2
states = {}
counter = 0

def get_id(text):
    global counter
    
    if text in states:
        return states[text]
    else:
        counter = counter + 1
        states[text] = counter
        return counter

print(get_id('cat'), get_id('dog'))