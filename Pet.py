class Puppy():
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def __str__(self):
        return f"{self.breed} puppy name is {self.name}"
    
ruffss = Puppy(name = "Ruffss", breed = "Beagle")
bibi = Puppy(name = "Bibi", breed = "Damatian")

print(ruffss)
print(bibi)