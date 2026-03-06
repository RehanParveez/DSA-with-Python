## adding all elements
# def sum_num(num):
#     answer = 0
#     for val in num:
#         answer = answer + val
#     return answer

# print(sum_num([1, 2, 3, 4, 6, 7, 8, 9, 5]))


## even numbers count in array

# def even(num):
#     count = 0
#     for val in num:
#         if val % 2 == 0:
#             count += 1
#     return count
# print(even([1, 2, 3, 4, 6, 7, 8, 9, 5]))


## average finding of the array elements
## 1
# def avg(num):
#     answer = 0
#     for val in num:
#         answer = answer + val
#     average = answer / len(num)
#     return average

# print(avg([1, 2, 3, 4, 6, 7, 8, 9, 5]))

## 2
# def avg(num):
#     answer = 0
#     full = len(num)
#     for val in num:
#         answer = answer + (val / full)
#     return answer

# print(avg([1, 2, 3, 4, 6, 7, 8, 9, 5]))


# index finding of an elment
# def element(num, target):
#     position = 0
#     for val in num:
#         if val == target:
#             return position
#         position += 1
#     return -1

# print(element([5,7,2,3,9,8,4], 8))


## all zeros to be moved to the End
# def move(num):
#     non_zero = []
#     zeros = []
#     for val in num:
#         if val == 0:
#             zeros.append(val)
#         else:
#             non_zero.append(val)
#     return non_zero + zeros

# print(move([6,0,2,0,9,0,1]))
        
        
## second largest number in an array
## 1
# def find(num):
#     largest = num[0]
#     for val in num:
#         if val > largest:
#             largest = val
#     num.remove(largest)
    
#     second_largest = num[0]
#     for val in num:
#         if val > second_largest:
#             second_largest = val
#     return second_largest

# print(find([5,7,2,3,9,8,4]))

## 2
# def find(num):
#     largest = num[0]
#     second_largest = num[0]
#     for val in num:
#         if val > largest:
#             second_largest = largest
#             largest = val
#         elif val > second_largest and val != largest:
#             second_largest = val
#     return second_largest

# print(find([5,7,2,3,9,8,4]))





    
        
    