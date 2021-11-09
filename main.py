#list data types

'''
Lists are mutable
lists are enclosed in square brackets
lists can contain different data types (int, str, boolean etc)
lists can contain duplicate items/List elements do not need to be unique.
Lists are ordered-items remain in an ordered sequence
'''

# list = []
# print (list)

# list = [1, 2, 3]
# print (list)

# list = ["apple","pears", "mangoes", "apple", "pineappples"] #duplicate items
# print(list)


# list = [1, True, "hello", 5.7899594995]#different data types
# print(list)

'''
list indexing

'''

# list = ["apple","pears", "mangoes", "apples", "pineappples"] 

# print(list[1]) #pears starts index from 0
# print (list[-1]) #gives pineapples starts from behind
# print(list[-2]) #gives apples


'''
Nesting of lists

'''

#lists within a list


# list = ["apple","pears", ["mangoes", "apples", "pineappples"]]


# print(list[2][1]) #to access second apples

# print(list[2][2]) #to access second pineapples



'''
How to Slice Lists in Python
'''

list = ["apple","pears", "mangoes", "apples", "pineappples"] 
# print(list[:]) #gives entire list
#print(list[:3]) #["apples", "pears", "mangoes"]
# print(list[1:]) #gives from index 1 to end
# print(list[2:2]) #empty it begins from index 2 to position 2
# print(list[:-2]) #gives ['apple', 'pears', 'mangoes']
# print(list[:-1]) #["apple","pears", "mangoes", "apples"]
#print(list[2:]) #['mangoes', 'apples', 'pineappples']
# every nth item
#print(list[::2]) #["apple", "mangoes",  "pineappples"] 
#print(list[::1]) # ["apple","pears", "mangoes", "apples", "pineappples"]  gives list as it is 
#print(list[::3]) # ["apple",  "apples"] 
#print(list[::-1])  #  ["pineappples", "apples","mangoes","pears",  "apple" ] #reversed order of items start from end to first item
#print(list[::-2]) #['pineappples', 'mangoes', 'apple'] reversed order skpping to second item every other item
#print(list[:-3]) #["apple","pears"]

'''

adding items to the list in python

'''
# list = ["apple","pears", "mangoes", "apples", "pineappples"] 
# list[1] ="melon"
# print(list) #replaced pears with melon

'''
append- adds item to the end of the list
'''

# list = ["apple","pears", "mangoes", "apples", "pineappples"]
# list.append("avocado") #append takes only one argument
# print(list)

'''
You can append using slicing
'''
# list = ["apple","pears", "mangoes", "apples", "pineappples"]
# list[1:3] = ["Alannah", "Merine", "Love"]
# print (list)


# list = ["apple","pears", "mangoes", "apples", "pineappples"]
# list[1:] = ["Alannah", "Merine", "Love"]
# print (list) #replaces everything after index 1


'''

Insert() method requires two arguments -index and the item
it inserts item before index
'''
# list = ["apple","pears", "mangoes", "apples", "pineappples"]
# list.insert(3, "Tomato")

# print(list) ##outcome -['apple', 'pears', 'mangoes', 'Tomato', 'apples', 'pineappples']


'''
To append elements from another list to the current list, use the extend() metlist = ["apple","pears", "mangoes", "apples", "pineappples"]hod.
'''

# list = ["apple","pears", "mangoes", "apples", "pineappples"]
# list_second = ["Alannah", "Merine", "Love"]

# list.extend(list_second)
# print(list) #output -['apple', 'pears', 'mangoes', 'apples', 'pineappples', 'Alannah', 'Merine', 'Love']



'''

extend allows you to add any iterable object (tuples, sets, dictionaries etc.).

'''
#list = ["apple","pears", "mangoes", "apples", "pineappples"]
# list_second = ("Alannah", "Merine", "Love") #tuple
#list.extend (list_second)
# print (list)  #outcome ['apple', 'pears', 'mangoes', 'apples', 'pineappples', 'Alannah', 'Merine', 'Love']



'''

remove 0r delete list items
Help on built-in function remove:

remove(value, /) method of builtins.list instance
    Remove first occurrence of value.

'''

# print(help(list.remove)) ' 


# list = ["apples","pears", "mangoes", "apples", "pineappples"]
# list.remove("apples")
# print(list)

'''
The pop() method removes the specified index.


'''

#more precise way of removing element 


# list = ["apples","pears", "mangoes", "apples", "pineappples"]
# list.pop(-2)  #removes second occurence of apples (index -2)
# print(list) 




'''
del keyword also removes the specified index. Just like pop(i)

'''


# list = ["apples","pears", "mangoes", "apples", "pineappples"]
# del list [2] #removes mangoes (item of index 2 position)
# print(list)





'''
del keyword is used to completely delete a list 

'''




# list = ["apples","pears", "mangoes", "apples", "pineappples"]
# del list
# print(list) #gives error as list shows no longer defined 




'''
clear () method  empties a list. unlike the del keyword, the list is still defined but empty

'''

# list = ["apples","pears", "mangoes", "apples", "pineappples"]
# list.clear()
# print(list)

'''
If you do not specify the index, the pop() method removes the last item.

'''
# list = ["apples","pears", "mangoes", "apples", "pineappples"]
# list.pop()  #removes last item 
# print(list)

# list = ["apples","pears", "mangoes", "apples", "pineappples"]
# print(list.index("apples") )



'''
to see all the methods for list 

print (dir(list))

'''

'''
#also to check what a method does use help

print(help(list.index)) -index(value, start=0, stop=9223372036854775807, /) method of builtins.li
st instance
    Return first index of value.

'''


# list = ["apples","pears", "mangoes", "apples", "pineappples"]
# pos= list.index("apples")
# list.pop(pos)
# print(list)



'''

print(help(list.count))
count(value, /) method of builtins.list instance
    Return number of occurrences of value.
'''
#list = ["apples","pears", "mangoes", "apples", "pineappples"]
#list.count("apples")
#print(list.count("apples"))  #outcome is 2
result = {}
for i in list:
  #print (i) #gives all items 
  result[i]= list.count(i)
print(result)



'''
counter -gives  output that will have the count of each element.

'''
# from collections import Counter
# list = ["apples","pears", "mangoes", "apples", "pineappples"]
# print(Counter(list))