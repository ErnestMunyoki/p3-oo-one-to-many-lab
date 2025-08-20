class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        if owner is not None and not isinstance(owner, __import__("lib.owner").owner.Owner):
            raise Exception("owner must be an instance of Owner")

        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        Pet.all.append(self)


from .pet import Pet

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return a list of all pets owned by this owner."""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign an Owner to a Pet if valid."""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self

    def get_sorted_pets(self):
        """Return pets sorted by their names."""
        return sorted(self.pets(), key=lambda pet: pet.name)
