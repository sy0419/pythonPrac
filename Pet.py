class Dog():
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

class Puppy(Dog):
    def __init__(self, name, breed):
        super().__init__(name, breed, 2)

    def __str__(self):
        return f"{self.breed} puppy name is {self.name} and I am {self.age}months years old."
    
ruffss = Puppy(name = "Ruffss", breed = "Beagle")
bibi = Puppy(name = "Bibi", breed = "Dalmatian")

print(ruffss)
print(bibi)