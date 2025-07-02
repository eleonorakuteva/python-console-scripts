"""
Project name: Pet Adoption Center Management System

System for a pet adoption center that manages pets, adopters, and staff members.
The center keeps track of available pets, and adopters can adopt or return pets.
Staff (workers) can add or remove pets from the center.
"""


class AdoptionCenter:
    def __init__(self, name:str, dict_of_pets = None):
        self.name = name
        self.dict_of_pets = dict_of_pets if dict_of_pets is not None else {}

    def __repr__(self):
        return (f"{self.name} is a adoption center, where you can adopt your future pet!\n"
                f"In the center there are registered animals: {self.dict_of_pets} ")

    def list_available_pets(self):
        return (f"Available pets you can adopt:\n"
                f"{self.dict_of_pets}")


class Pet:
    def __init__(self, name:str, species:str, age:int):
        self.name = name
        self.species = species
        self.age = age
        self.is_adopted = False

    def pet_dict(self):
        return {self.species :
                    [{"name" : self.name}, {"age" : self.age}]
                }

    def search_by_species(self):
        matches = {key, value for key, value in self.pet_dict}
        return matches

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

    def is_id_valid(self):
        return len(self._worker_id) == 8 and self._worker_id.isdigit()

    def add_pet(self, pet, adoption_center):
        if self.is_id_valid():
            pass

    def remove_pet(self, pet, adoption_center):
        if self.is_id_valid():
            pass

    def __repr__(self):
        return (f"Worker name: {self.name}.\n"
                f"Worker Id: {self._worker_id}, valid = {self.is_id_valid()}.")


if __name__ == "__main__":
    center = AdoptionCenter("SunnyPaws")

    pet1 = Pet("Bella", "Dog", 3)
    pet2 = Pet("Luna", "Cat", 1)

    worker = Worker("James", "10001023")
    adopter = Adopter("Maria", "10001024")
    print(worker)

    worker.add_pet(pet1, center)
    worker.add_pet(pet2, center)

    center.list_available_pets()

    adopter.adopt_pet(pet1, center)
    center.list_available_pets()

    # adopter.return_pet(pet1, center)
    # center.list_available_pets()
