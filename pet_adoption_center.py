"""
Project name: Pet Adoption Center Management System

"""
class AdoptionCenter:
    def __init__(self, name:str):
        self.name = name
        self.list_of_pets = None

    def __repr__(self):
        return (f"{self.name} is a adoption center, where you can adopt your future pet!\n"
                f"In the center there are registered animals: {", ".join(self.list_of_pets)} ")

class Pet:
    def __init__(self, name:str, species:str, age:int):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False