# # simple inheritance

# # base class

# class Animal:
#     def __init__(self,name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound")

# # derived class
# class Dog(Animal):

#     def speak(self):
#         print(f"{self.name} barks.")

# #create an instance of animal
# animal = Animal("generic animal")
# animal.speak()

# # create an instance of dog
# dog = Dog()
# dog.speak()


# super keywoerd

class Animal:
    def __init__(self):
        self.name = "buddy"

    def speak(self):
        print(f"{self.name} makes a sound")

# derived class
class Dog(Animal):

    def __init__(self, breed):
        super().__init__()
        self.breed = breed

    def speak(self):
        super().speak() #calls the base class method
        print(f"{self.name} barks. it is a {self.breed}")

dog = Dog("Desi breed")
dog.speak()