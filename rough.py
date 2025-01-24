lst = [1,2,3]
mystr = "mlops"
my_int = 134

# print(type(my_int))
# lst.clear()
# mystr = mystr.capitalize()

# print(mystr)

from oops_proj import chatbook
user1 = chatbook()
print(user1.id)

# using static method directly from class rather than obj
# chatbook.set_id(10)

# user2 = chatbook()
# print(user2.id)

# user3 = chatbook()
# print(user3.id)


# encapsulation, getter and setter
 # print(user2._chatbook__name)
# print(user2.get_name())
# user2.set_name("hello")
# print(user2.get_name())




#function vs method
# lst = [1,2,4]

# a1 = len(lst) #function
# print(a1)

# user1 = chatbook()
# user1.send_message() #method