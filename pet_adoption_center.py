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

    def list_available_pets(self):
        pass

    def list_all_pets(self):
        pass

class Pet:
    def __init__(self, name:str, species:str, age:int):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

class Adopter:
    def __init__(self, name:str):
        self.name = name
        self.list_of_pets = None

    def adopt_pet(self, pet:str, center:str):
        pass

    def return_pet(self, pet:str, center:str):
        pass

class Worker(Adopter):
    def __init__(self, name:str, worker_id:str):
        super().__init__(name)
        self.worker_id = worker_id

    def add_pet(self, pet, center):
        pass

    def remove_pet(self, pet, center):
        pass