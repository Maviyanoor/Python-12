# # wrong method
# name = "Maviya"
# name = 700 # This is wrong but not generating error
# print(name) # print
# print(type(name)) # type of name
# print(id(name)) # physical address
# print([i for i in dir(name)]) # methods and attributes

# # correct method
# name:int = 700
# print(name)

# name: list[str] = ['a','b','c',200] # error just string pass
# print(name)
# print(type(name))
# print(id(name))
# print(dir(name))

# name: list[str, int , float] = ('Maviya', 200 , "abc")
# print(name)
# print(type(name))
# print(id(name))
# print(dir(name))


name: any = "pakistan"
print(name)
print(type(name))
print(id(name))
print(dir(name))

       

