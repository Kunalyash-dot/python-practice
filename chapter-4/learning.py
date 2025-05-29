# List & tuples 

# Lists : it is container to store a set of values of any data type.

samples=["kunal","Amith","Harry","peter",7,True,{"name":"Kunal","age":18}]

# append
# samples.append(17)
# print(samples) #['kunal', 'Amith', 'Harry', 'peter', 7, True, {'name': 'Kunal', 'age': 18}, 17]

# Extend
more_list=["rohit","Kamal"]
# samples.extend(more_list)
# print(samples) # ['kunal', 'Amith', 'Harry', 'peter', 7, True, {'name': 'Kunal', 'age': 18}, 17, 'rohit', 'Kamal']

# insert
# samples.insert(3,"Added in third index")
# print(samples)  # ['kunal', 'Amith', 'Harry', 'Added in third index', 'peter', 7, True, {'name': 'Kunal', 'age': 18}]

# remove
# samples.remove("kunal")
# print(samples)

# pop
# last_value = samples.pop()
# print(last_value)
# print(samples)


# clear
# samples.clear()
# print(samples)

# index
# print(samples.index("Harry"))

# count 
num=[2,1,3,5,6,9,2,10,2]
# count=num.count(2)
# print(count)


# sort
num.sort()
# print(num)

# reverse

# num.reverse()
# print(num)
# samples.reverse()
# copy 
# sample_copy=samples.copy()
# samples.append("check")
# print(samples)
# print(sample_copy)


# tuples

a=()  # empty tuple
b=(1,) # tuple with one element
c=(1,3,5,7,8,2,10,2,10,20,10)

# print(len(c))
# print(c.count(10))
print(c.index(10))
