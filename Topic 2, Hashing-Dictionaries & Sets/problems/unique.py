## Q Problem: first unique character at index
##1
# def unique(idx):
#     known = {}
#     for val in range(len(idx)):
#       if idx[val] not in known:
#         known[idx[val]] = 1
#         return val
#     return -1

# print(unique('swiss bliss'))

## 2
def unique(idx):
    count = {}
    for ch in idx:
      if ch in count:
          count[ch] += 1
      else:
          count[ch] = 1
          
    for val in range(len(idx)):
        if count[idx[val]] == 1:
            return val
    return -1

print(unique('swiss bliss'))