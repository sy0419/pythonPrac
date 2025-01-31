class Dog():
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

class Puppy(Dog):
    def __str__(self):
        return f"{self.breed} puppy name is {self.name} and I am {self.age}months years old."
    
ruffss = Puppy(name = "Ruffss", breed = "Beagle", age = 1)
bibi = Puppy(name = "Bibi", breed = "Dalmatian", age = 3)

print(ruffss)
print(bibi)