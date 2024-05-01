class Organism:
    species = "unknown"

    def __init__(self, species="unknown"):
        self.species = species

adam = Organism(species="Human")

print(adam.species) # Human



class Fairy(Organism):
    species = "Fairy"

    def __init__(self, species="Fairy"):
        super().__init__(species) # this is calling the __init__ of the parent class
    

avii = Fairy()
print(avii.species) # Fairy

class Student(Organism):
    species = "Human"

    def __init__(self, name, age):
        super().__init__(self.species) # this is calling the __init__ of the parent class
        # so we are here now!!!
        print(f"this is name, age, species {name}, {age}, {self.species}")
        # now you had these variables in this __init__ function only for now till this step
        self.name = name
        self.age = age
    
    def talk(self):
        return f"Hello, my name is {self.name}"



ironman = Student("Tony Stark", 40) # when i call this, the __init__ runs with the parameters
abizz = Student("Abizz", 20)

print(ironman.name)
print(abizz.name)

print(ironman.species)
print(abizz.species)


print(ironman.talk())
print(abizz.talk())
