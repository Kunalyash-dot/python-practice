# Dictionary & sets

# Dictionary - is a collection of key-value pairs.
my_dict={"a":1,"b":2,"c":3}

# methods

# clear
# my_dict.clear()
# print(my_dict)

# copy 

shallow_copy= my_dict.copy()
print(shallow_copy)

# get 

# print(my_dict.get("a"))  # output - 1
# print(my_dict.get("d"))  #output - none
# print(my_dict.get("d","default value it could be string or number")) 

# items 

# print(my_dict.items()) # dict_items([('a', 1), ('b', 2), ('c', 3)])

# keys

# print(my_dict.keys()) # dict_keys(['a', 'b', 'c'])

# values 

# print(my_dict.values())

# pop 

# print(my_dict.pop("b"))
# print(my_dict)

# popItem 

# print(my_dict.popitem())

# update 

# my_dict.update({"d":4})
# print(my_dict)

# setdefault 

# print(my_dict.setdefault("e",5))  
# print(my_dict)

