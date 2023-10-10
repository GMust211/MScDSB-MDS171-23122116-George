class PetStore:
    def __init__(self):
        self.pet = {}

    def store_pet(self, name, species, age, price):
        pet_id = len(self.pet) + 1
        self.pet[pet_id] = {
            'name': name,
            'species': species,
            'age': age,
            'price': price
        }
        print(f"Pet {name} added to the inventory.")

    def search_pet(self, name):
        for pet_id, pet_info in self.pet.items():
            if pet_info['name'].lower() == name.lower():
                return pet_id, pet_info
        return None

    def sell_pet(self, pet_id):
        if pet_id in self.pet:
            pet_info = self.pet.pop(pet_id)
            print(f"Sold pet {pet_info['name']} for ${pet_info['price']}.")
        else:
            print("Pet not found in inventory.")

    def list_pets(self):
        print("Available Pets:")
        for pet_id, pet_info in self.pet.items():
            print(f"ID: {pet_id}, Name: {pet_info['name']}, `Species`: {pet_info['species']}, Age: {pet_info['age']}, Price: ${pet_info['price']}")
