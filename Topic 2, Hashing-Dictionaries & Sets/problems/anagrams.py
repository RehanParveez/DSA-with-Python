## Q Problem: group the words with same letter pattern
## 1
# def grouping(words):
#    groups = []
#    for word in words:
#       example = []
#       for other in words:
#          if sorted(word) == sorted(other):
#             example.append(other)
#       groups.append(example)
#    return groups

# print(grouping(['stone','tones','notes','hello','below','elbow']))

## 2
def grouping(words):
    groups = {}
    for word in words:
      key = "".join(sorted(word))
      if key in groups:
        groups[key].append(word)
      else:
         groups[key] = [word]
         
    return list(groups.values())

print(grouping(['stone','tones','notes','hello','below','elbow']))
