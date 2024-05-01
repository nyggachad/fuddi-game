class Student:
    species = "Human" # this is a class variable

    def __init__(self, name, age, species="Human"):
        # so we are here now!!!
        print(f"this is name, age, species {name}, {age}, {species}")
        # now you had these variables in this __init__ function only for now till this step
        self.name = name
        self.age = age
        self.species = species
    
    def talk(self):
        return f"Hello, my name is {self.name}"



ironman = Student("Tony Stark", 40, "alligato") # when i call this, the __init__ runs with the parameters
abizz = Student("Abizz", 20)

print(ironman.name)
print(abizz.name)

print(ironman.species)
print(abizz.species)


print(ironman.talk())
print(abizz.talk())
