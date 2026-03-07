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


## removing duplicates from array
## 1
# def duplicate(num):
#     nums = []
#     for val in num:
#         found = False
#         for v in nums:
#             if v == val:
#                 found = True
#         if found == False:
#             nums.append(val)
#     return nums

# print(duplicate([1,2,2,3,4,4,5]))

## 2
# def duplicate(num):
#     result = []
#     for val in num:
#         if val not in result:
#             result.append(val)
#     return result
 
# print(duplicate([1,2,2,3,4,4,5]))


## finding the missing number
## 1
# def missing(nums):
#     val = 1
#     while True:
#        count = 0
#        for v in nums:
#           if v == val:
#              count = count + 1
#           if count == 0:
#             return val
#        val += 1

# print(missing([2,3,4,5,6,8,9]))

## 2 
# def missing(nums):
#     largest = nums[0]
#     for val in nums:
#        if val > largest:
#           largest = val
#     for v in range(1, largest + 1):
#        if v not in nums:
#           return v

# print(missing([2,3,4,5,6,8,9]))


## finding the pairs that have sum same as target
# ## 1
# def pairs(num, target):
#     val = 0
#     while val < len(num):
#         v = 0
#         while v < len(num):
#             if val != v:
#               if num[val] + num[v] == target:
#                 print(num[val], num[v])
#             v += 1
#         val += 1

# pairs([2,4,3,5,7,8], 9)

# ##2
# def pairs(num, target):
#     for val in range(len(num)):
#        for v in range(val + 1, len(num)):
#           if num[val] + num[v] == target:
#             print(num[val], num[v])

# print(pairs([2,4,3,5,7,8], 9))


## rotating the array by one position
## 1
# def rotate(nums):
#     num = []
#     last = nums[len(nums)]
#     num.append(last)
#     val = 0
#     while val < len(nums):
#         num.append(nums[val])
#         val += 1
#     return num
#
# print(rotate([4,2,5,9,7]))

## 2
# def rotate(nums):
#     last = nums[len(nums) - 1]
#     num = len(nums) - 1
#     while num > 0:
#         nums[num] = nums[num - 1]
#         num -= 1
#     nums[0] = last
#     return nums

# print(rotate([4,2,5,9,7]))

        
            
            





    
        
    