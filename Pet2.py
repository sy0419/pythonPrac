class Cat():
    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

class kitten(Cat):
    def __init__(self, name, breed):
        super().__init__(name, breed, 1)

    def __str__(self):
      return f"My name is {self.name} and I am {self.age}month(s) {self.breed} kitten."

mini = kitten(name = "Mini", breed = "Ragdoll")

print(mini)