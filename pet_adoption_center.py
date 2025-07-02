"""
Project name: Pet Adoption Center Management System

System for a pet adoption center that manages pets, adopters, and staff members.
The center keeps track of available pets, and adopters can adopt or return pets.
Staff (workers) can add or remove pets from the center.
"""
class AdoptionCenter:
    def __init__(self, name:str, list_of_pets = None):
        self.name = name
        self.list_of_pets = list_of_pets if list_of_pets is not None else []

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
    def __init__(self, name:str, adopted_pets_by_user = None):
        self.name = name
        self.adopted_pets_by_user = adopted_pets_by_user if adopted_pets_by_user is not None else []

    def adopt_pet(self, pet:str, center:str):
        pass

    def return_pet(self, pet:str, center:str):
        pass

    def user_adopted_pets(self):
        pass

    def __repr__(self):
        return (f"Adopter name: {self.name}.\n"
                f"Adopted pets: {", ".join(self.adopted_pets_by_user)}.")

class Worker(Adopter):
    def __init__(self, name:str, worker_id:str, adopted_pets_by_user = None):
        super().__init__(name, adopted_pets_by_user)
        self._worker_id = worker_id

    def add_pet(self, pet, center):
        pass

    def remove_pet(self, pet, center):
        pass

    def __repr__(self):
        return (f"Worker name: {self.name}.\n"
                f"Worker Id: {self._worker_id}.")