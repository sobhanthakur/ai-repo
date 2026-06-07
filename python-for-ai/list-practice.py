# nums = [5, 1, 5, 2, 5, 3]
# count = 0
# for i in range(0,len(nums)):
#     if nums[i] == 5:
#         count += 1
# print(count)

# animals = ["dog", "cat", "lion"]
# print(animals.index("cat"))

# fruits = ["apple", "banana"]
# fruits.insert(1,"grapes")
# fruits.append("Plum")
# print(fruits)

# fruits = ["apple", "banana", "orange"]
# del fruits[fruits.index("banana")]
# print(fruits)

# nums = [5,6,1, 2, 3, 4]
# nums.reverse()
# print(nums)

# nums = [5,6,1, 2, 3, 4]
# nums.sort()
# print(nums)

# nums = [4, 8, 1, 9, 2]
# # maximum = max(nums)
# maximum=-1
# for i in range(0,len(nums)):
#     if nums[i] > maximum:
#         maximum = nums[i]
# print(maximum)

# nums = [1, 2, 3, 4]
# squares = []
# for i in range(0,len(nums)):
#     squares.append(nums[i]**2)
# print(squares)

# a = [1, 2, 3]
# b = a.copy()
# print(b)
# print (a == b)
# print (a is b)


# nums = [1, 2, 2, 3, 1, 4]
# dedup=[]
# for i in range(0,len(nums)):
#     if nums[i] not in dedup:
#         dedup.append(nums[i])
# print(dedup)

# nums = [1, -2, 3, -4, 5]
# pos=0
# neg=0
# for i in range(0,len(nums)):
#     if nums[i] < 0:
#         neg += 1
#     else:
#         pos += 1
# print(f"{pos=} {neg=}")

# nums = [1, 2, 3, 4]
# sum = 0
# for i in range(0,len(nums)):
#     sum += nums[i]
# print(f"{sum=}")

# nums = [10, 20, 4, 45, 99]
# maximum = max(nums)
# second = -1
# for i in range(0,len(nums)):
#     if nums[i] > second and nums[i] != maximum:
#         second = nums[i]
# print(second)

# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# for i in range(0,len(a)):
#     if a[i] in b:
#         print(f"{a[i]}")

# nums = [1, 2, 3, 4]
# rotate = nums[1:len(nums)]
# rotate.append(nums[0])
# print(rotate)

# a = [1, 2]
# b = [3, 4]
# a.extend(b)
# a.sort(reverse=True)
# print(a)

# nums = [5,4,1,2,3]
# new_arr = sorted(nums,reverse=True)
# print (new_arr)

a = [3, 1]
b = [4, 2]
a.extend(b)
a.sort()
print(a)