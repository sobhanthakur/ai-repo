# dict = "I love python python"
# words = dict.split(' ')
# freq = {}
# for i in range(0,len(words)):
#     if words[i] in freq:
#         freq[words[i]] += 1
#     else:
#         freq[words[i]] = 1
# print(freq)

# d1 = {'a':2, 'b':3}
# d2 = {'a':5, 'c':1}
# for key,value in d1.items():
#     if key in d2:
#         d1[key] += d2[key]
# for key,value in d2.items():
#     if key not in d1:
#         d1[key] = d2[key]
# print (d1)

# fruits = ["apple", "ant", "bat", "ball"]
# dict = {}
# for i in range(0,len(fruits)):
#     if fruits[i][0] in dict:
#         dict[fruits[i][0]].append(fruits[i])
#     else:
#         dict[fruits[i][0]] = [fruits[i]]        
# print(dict)

dict = {'a':1,'b':2}
print(dict.get('a'))
print(dict.items())
