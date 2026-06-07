# class Dog:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#     def print_name(self):
#         return f"{self.name}"
    
# dog = Dog(name="GS",color="black")
# print(dog.print_name())

print(type(1))


class Dog:
    species = "canine"

    def __init__(self , species):
        self.species = species

    # @classmethod
    def get_species(self):
        return self.species

d = Dog("Sobhan")
print(d.get_species())