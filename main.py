class Organism:
    species = "unknown"
    message = "bla bla bla"
    hp = 100
    attack = 10

    def __init__(self, species="unknown"):
        self.species = species
    
    def talk(self):
        return self.message
    
    def hit(self, opponent):
        print(f"{self} hits {opponent}")

class Fairy(Organism):
    species = "Fairy"
    message = "I am a fairy uwu"

    def __init__(self, species="Fairy"):
        super().__init__(species) # this is calling the __init__ of the parent class

class Student(Organism):
    species = "Human"
    message = "I am a student"

    def __init__(self, name, age):
        super().__init__(self.species) # this is calling the __init__ of the parent class
        # so we are here now!!!
        print(f"this is name, age, species {name}, {age}, {self.species}")
        # now you had these variables in this __init__ function only for now till this step
        self.name = name
        self.age = age
    
    def talk(self):
        return f"Hello, my name is {self.name}"
    
    

if __name__ == "__main__":
    # initiallizing the classes
    adam = Organism(species="Human")
    hao = Student("Hao", 19)
    avii = Fairy()
    ironman = Student("Tony Stark", 19) # when i call this, the __init__ runs with the parameters
    abizz = Student("Abizz", 17)

    objects = [adam, hao, avii, ironman, abizz]

    print("----------printing species---------")
    # printing species
    for obj in objects:
        print(obj.species)

    print("---------printing names---------")
    # printing names
    for obj in objects:
        if isinstance(obj, Student): # it checks if the object is from the Student class
            print(obj.name)

    print("---------printing talk---------")
    # printing talk
    for obj in objects:
        print(obj.talk())


    print("---------printing hp---------")
    # printing hp
    for obj in objects:
        print(obj.hp) # this will print 100 for all the objects


    # hao hits avii
    hao.hit(avii)

    print("---------printing hp after hit---------")
    # printing hp
    for obj in objects:
        print(obj.hp) # this will print 100 for all the objects
