list = ['a','b']
for i in range(0,len(list)):
    print(list[i])
    
print(list[-2])


fruits = ["apple", "banana", "orange"]

# Get items
print(fruits[0])  
print(fruits[1]) 
print(fruits[-1]) 
print(fruits[-2]) 

# Slicing
print(fruits[0:2])
print(fruits[1:])

fruits.remove("banana") 
print(fruits[0:len(fruits)])

last = fruits.pop()        # Remove and return last
print(fruits[0:len(fruits)])

del fruits[0] 
print(fruits[0:len(fruits)])

# Check if item exists
if "apple" in fruits:
    print("Found apple!")

# Check if list is empty
if fruits:
    print("List has items")
else:
    print("List is empty")
    
num_list = [0,2,3,4,5]

if 1 in num_list:
    print("1 is available")
else:
    print("1 is not available")
    
num_list1 = [0,2,3,4,5]
del num_list1[num_list1.index(4)]
print(num_list1)
