# initiate a class
class employee:
    # special/magic/dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"

    def travel(self, destination):
        print(f"Employee is travelling to {destination}")



#  create an object/instance of class
sam = employee()

#printing the attributes
# print(sam.id)

# calling a method
# sam.travel("london")

print(type(sam))